from django.contrib import admin
from django.urls import path, include
from docs.views import schema_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
    path('partner/', include('partners.urls')),
    path('client/', include('clients.urls')),
    path('reviews/', include('reviews.urls')),
    path('feedbacks/', include('feedbacks.urls')),
    path('menus/', include('menus.urls'))
]

urlpatterns += [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)