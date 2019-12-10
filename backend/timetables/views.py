from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from timetables.models import BusinessHour
from timetables.serializers import BusinessHourSerializer

class ListCreateBusinessHourAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessHourSerializer

    def get_queryset(self):
        queryset = BusinessHour.objects.filter(store=self.kwargs.get('store_id'))
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('bhours_id'))
        return obj

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '영업시간 등록 완료', 'data': serializer.data}
        return Response(body, status=status.HTTP_201_CREATED)


class RetrieveUpdateBusinessHourAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessHourSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['bhours_id'])
        return obj