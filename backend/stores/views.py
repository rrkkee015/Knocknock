from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.db.models import Q, F

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from stores.models import Category, Store
from stores.serializers import (
    CategorySerializer,
    StoreByDistanceSerializer,
    StoreListSerializer,
    StoreDetailSerializer
)
from clients.models import Review
from reviews.serializers import ReviewSerializer
from menus.models import Menu
from menus.serializers import MenuSerializer
from datetime import datetime, timedelta


class StoreByDistanceListAPI(generics.ListAPIView):
    serializer_class = StoreByDistanceSerializer

    def get_queryset(self):
        location = self.request.query_params.get('loc')
        lat, lon = map(float, location.split(','))
        pnt = GEOSGeometry(f'POINT({lat} {lon})', srid=4326)
        queryset = Store.objects.annotate(distance=Distance('location', pnt))
        return queryset

    def filter_queryset(self, queryset):
        if self.request.query_params.get('d') and self.request.query_params.get('hour'):
            distance = self.request.query_params.get('d')
            queryset = queryset.filter(Q(distance__lte=distance))

            hour = self.request.query_params.get('hour')
            time = datetime.strptime(
                (datetime.now()+timedelta(hours=int(hour))).strftime('%H:%M'), '%H:%M').time()
            day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
            today = datetime.now().weekday()
            yesterday = (datetime.now() - timedelta(days=1)).weekday()
            before_midnight_queryset = queryset.filter(
                # 요청 당일
                Q(business_hours__day__exact=day[today])
                # 휴무 여부
                & Q(business_hours__is_dayoff=False)
                # 오늘 영업 마감
                & Q(business_hours__start__lt=F('business_hours__end'))
                # 영업 시작시간이 현재 시간을 포함한 이전
                & Q(business_hours__start__lte=time)
                # 영업 종료시간이 현재 시간 이후
                & Q(business_hours__end__gt=time)
                & (
                    # 브레이크 시작시간이 현재 시간 이후
                    Q(business_hours__start_break__gt=time)
                    # 브레이크 종료시간이 현재시간을 포함한 이전
                    | Q(business_hours__end_break__lte=time)
                    # 브레이크 시작시간이 없음
                    | Q(business_hours__start_break__isnull=True)
                    # 브레이크 종료시간이 없음
                    | Q(business_hours__end_break__isnull=True)
                )
                & (
                    # 라스트오더 시간이 현재 시간 이후
                    Q(business_hours__last_order__gt=time)
                    # 라스트오더가 없음
                    | Q(business_hours__last_order__isnull=True)
                )
            )
            after_midnight_queryset = queryset.filter(
                # 요청 당일
                Q(business_hours__day__exact=day[today])
                # 휴무 여부
                & Q(business_hours__is_dayoff=False)
                # 내일 새벽 영업 마감 또는 24시간 영업
                & Q(business_hours__start__gte=F('business_hours__end'))
                # 영업 시작시간이 현재 시간을 포함한 이전
                & Q(business_hours__start__lte=time)
                & (
                    # 브레이크 시작시간이 현재 시간 이후
                    Q(business_hours__start_break__gt=time)
                    # 브레이크 종료시간이 현재 시간을 포함한 이전
                    | Q(business_hours__start_break__isnull=True)
                    # 브레이크 시작시간이 없음
                    | Q(business_hours__end_break__lte=time)
                    # 브레이크 종료시간이 없음
                    | Q(business_hours__end_break__isnull=True)
                )
            )
            yesterday_after_midnight_queryset = queryset.filter(
                # 요청 전일
                Q(business_hours__day__exact=day[yesterday])
                # 휴무여부
                & Q(business_hours__is_dayoff=False)
                # 오늘 새벽 영업 마감 또는 24시간 영업
                & Q(business_hours__start__gte=F('business_hours__end'))
                # 영업 종료시간이 현재 시간 이후
                & Q(business_hours__end__gt=time)
                & (
                    # 브레이크 시작시간이 현재 시간 이후
                    Q(business_hours__start_break__gt=time)
                    # 브레이크 종료시간이 현재 시간 이후
                    | Q(business_hours__start_break__isnull=True)
                    # 브레이크 시작시간이 없음
                    | Q(business_hours__end_break__lte=time)
                    # 브레이크 종료시간이 없음
                    | Q(business_hours__end_break__isnull=True)
                )
                & (
                    # 라스트오더 시간이 현재 시간 이후
                    Q(business_hours__last_order__gt=time)
                    # 라스트오더 시간이 없음
                    | Q(business_hours__last_order__isnull=True)
                )
            )
            now_open_stores_queryset = before_midnight_queryset.union(
                after_midnight_queryset).union(yesterday_after_midnight_queryset)
            return now_open_stores_queryset.order_by('distance')[:100]
        return queryset.order_by('distance')[:100]


class StoreListAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        return queryset

    def filter_queryset(self, queryset):
        if self.request.query_params.get('name'):
            name = self.request.query_params.get('name')
            queryset = queryset.filter(Q(name__icontains=name))
        return queryset[:100]


class StoreDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['store_id'])
        return obj

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_cnt += 1
        obj.save()
        return self.retrieve(request, *args, **kwargs)


class ListStoreReviewAPI(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.filter(store=self.kwargs.get('store_id'))
        return queryset.order_by('-id')


class ListStoreMenuAPI(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.objects.filter(store=self.kwargs.get('store_id'))
        return queryset
