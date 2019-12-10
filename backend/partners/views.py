from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from accounts.models import Partner
from stores.models import Store
from stores.serializers import StoreListSerializer, StoreDetailSerializer
from partners.models import BusinessRegistration, Feedback
from partners.serializers import RegisterBusinessRegistration
from feedbacks.serializers import FeedbackSerializer
from clients.models import Review
from reviews.serializers import ReviewSerializer
from menus.models import Menu
from menus.serializers import MenuSerializer


class PartnerStoreListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreListSerializer

    def get_queryset(self):
        queryset = Store.objects.filter(partner__user=self.request.user).order_by('-id')
        return queryset


class PartnerStoreDetailAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)         # 자기 자신만 가능한 권한도 추가해야됨
    serializer_class = StoreDetailSerializer

    def get_queryset(self):
        return Store.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['store_id'])
        return obj


class BusinessRegistrationAPI(generics.GenericAPIView):
    # parser_class = (MultiPartParser, FormParser, FileUploadParser,)
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterBusinessRegistration

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            body = {'message': '파트너 등록 완료', 'body': serializer.data}
            return Response(body, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListStoreReviewAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.filter(store=self.kwargs.get('store_id'))
        return queryset.order_by('-id')


class ListReviewFeedbackAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = Feedback.objects.filter(review=self.kwargs.get('review_id'))
        return queryset.order_by('-id')


class ListStoreMenuAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.objects.filter(store=self.kwargs.get('store_id'))
        return queryset