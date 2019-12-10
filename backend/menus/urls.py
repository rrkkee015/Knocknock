from django.urls import path

from menus.views import (
    CreateMenuAPI,
    RetrieveUpdateDestroyMenuAPI
)

urlpatterns = [
    path('', CreateMenuAPI.as_view(), name='create_menu'),
    path('<int:menu_id>/', RetrieveUpdateDestroyMenuAPI.as_view(), name='retrieve_update_delete_menu')
]