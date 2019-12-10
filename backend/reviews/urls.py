from django.urls import path
from reviews.views import (
    ListCreateReviewAPI,
    RetrieveUpdateDestroyReivewAPI
)


urlpatterns = [
    path('', ListCreateReviewAPI.as_view(), name='list_create_review'),
    path('<int:review_id>/', RetrieveUpdateDestroyReivewAPI.as_view(), name='retrieve_update_delete_review'),
]