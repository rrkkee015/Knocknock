from django.contrib import admin
from accounts.models import Client, Partner

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    search_fields = ('user__username', 'nickname')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'phone',)
    list_display_links = ('id', 'user', 'name', 'phone',)
    search_fields = ('user__username', 'name', 'phone',)
    