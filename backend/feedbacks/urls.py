from django.urls import path
from feedbacks.views import (
    ListCreateFeedbackAPI,
    RetrieveUpdateDestroyFeedbackAPI
)

urlpatterns = [
    path('', ListCreateFeedbackAPI.as_view(), name='list_create_feedback'),
    path('<int:feedback_id>/', RetrieveUpdateDestroyFeedbackAPI.as_view(), name='retrieve_update_destory_feedback')
]