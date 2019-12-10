from django.urls import path
from partners.views import (
    PartnerStoreListAPI,
    PartnerStoreDetailAPI,
    BusinessRegistrationAPI,
    ListStoreReviewAPI,
    ListReviewFeedbackAPI,
    ListStoreMenuAPI
)
from timetables.views import (
    ListCreateBusinessHourAPI,
    RetrieveUpdateBusinessHourAPI
)

urlpatterns = [
    path('stores/', PartnerStoreListAPI.as_view(), name='manage_store_list'),
    path('stores/<int:store_id>/', PartnerStoreDetailAPI.as_view(), name='manage_store_detail'),
    path('stores/<int:store_id>/reviews/', ListStoreReviewAPI.as_view(), name='list_client_reviews'),
    path('stores/<int:store_id>/reviews/<review_id>/feedbacks/', ListReviewFeedbackAPI.as_view(), name='list_review_feedbacks'),
    path('stores/<int:store_id>/bhours/', ListCreateBusinessHourAPI.as_view(), name='list_create_business_hour'),
    path('stores/<int:store_id>/bhours/<int:bhours_id>/', RetrieveUpdateBusinessHourAPI.as_view(), name='retrieve_update_business_hour'),
    path('stores/<int:store_id>/menus/', ListStoreMenuAPI.as_view(), name='list_store_menus'),
    path('regist/', BusinessRegistrationAPI.as_view(), name='register_business_registration')
]