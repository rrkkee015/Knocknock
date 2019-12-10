from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from clients.models import Review
from reviews.serializers import ReviewSerializer


class ListCreateReviewAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.filter(client__user=self.request.user).order_by('-id')
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        if len(request.data['content']) < 1:
            body = {'message': '내용을 입력해주세요'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '리뷰 작성 완료', 'body': serializer.data}
        return Response(body, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyReivewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('review_id'))
        return obj
