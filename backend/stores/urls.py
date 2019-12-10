from django.urls import path
from stores.views import (
    StoreByDistanceListAPI,
    StoreListAPI,
    StoreDetailAPI,
    ListStoreReviewAPI,
    ListStoreMenuAPI
)

urlpatterns = [
    path('', StoreByDistanceListAPI.as_view(), name='store_list'),
    path('<int:store_id>/', StoreDetailAPI.as_view(), name='store_detail'),
    path('<int:store_id>/reviews/', ListStoreReviewAPI.as_view(), name='list_reviews'),
    path('<int:store_id>/menus/', ListStoreMenuAPI.as_view(), name='list_menus'),
    path('search/', StoreListAPI.as_view(), name='search_store'),
]