from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from clients.models import Review
# from clients.serializers import ReviewSerializer


# class RetrieveCreateReviewAPI(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         queryset = Review.objects.filter(store_id=self.kwargs['store_id'])
#         return queryset.order_by('-created_at')

#     def get(self, request, *args, **kwargs):
#         serializer = self.get_serializer(self.get_queryset(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         if len(request.data['content']) < 1:
#             body = {'message': '내용을 입력해주세요'}
#             return Response(body, status=status.HTTP_400_BAD_REQUEST)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         body = {'message': '리뷰 작성 완료', 'body': serializer.data}
#         return Response(body, status=status.HTTP_201_CREATED)


# class DeleteReivewAPI(generics.GenericAPIView):
#     queryset = Review.objects.all()
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, *args, **kwargs):
#         obj = get_object_or_404(self.get_queryset(), id=kwargs['review_id'])
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ReviewListAPI(generics.ListAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # 리뷰작성하지 않은사람은 에러 말고 빈 쿼리셋 뿌려줘야됨!!!
#         queryset = get_list_or_404(Review.objects.order_by('id'), client__user=self.request.user)
#         return queryset


# class ReviewDetailAPI(generics.RetrieveDestroyAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         obj = get_object_or_404(Review, pk=self.kwargs['review_id'])
#         return obj
