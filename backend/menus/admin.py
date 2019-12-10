from django.contrib import admin
from menus.models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'name', 'price',)
    list_display_links = ('id', 'store', 'name',)
    search_fields = ('store__name', 'name',)