from django.contrib import admin
from clients.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'client', 'content', 'created_at')
    list_display_links = ('id', 'store', 'client', 'content',)
    list_filter = ('client',)