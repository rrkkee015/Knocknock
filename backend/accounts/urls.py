from django.urls import path
from accounts.views.client_views import (
    ClientSignupAPI,
    ClientLoginAPI,
    ClientUserAPI,
    ClientLogoutAPI
)
from accounts.views.partner_views import (
    PartnerSignupAPI,
    PartnerLoginAPI,
    PartnerUserAPI,
    PartnerLogoutAPI,
)


urlpatterns = [
    path('client/signup/', ClientSignupAPI.as_view(), name='client_signup'),
    path('client/login/', ClientLoginAPI.as_view(), name='client_login'),
    path('client/auth/', ClientUserAPI.as_view()),
    path('client/logout/', ClientLogoutAPI.as_view(), name="client_logout"),

    path('partner/signup/', PartnerSignupAPI.as_view(), name='partner_signup'),
    path('partner/login/', PartnerLoginAPI.as_view(), name='partner_login'),
    path('partner/auth/', PartnerUserAPI.as_view()),
    path('partner/logout/', PartnerLogoutAPI.as_view(), name="partner_logout")
]

