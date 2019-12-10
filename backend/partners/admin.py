from django.contrib import admin
from partners.models import BusinessRegistration, Feedback

@admin.register(BusinessRegistration)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'company_name', 'representative_name', 'business_registration_number',)
    list_display_links = ('id', 'store', 'company_name', 'representative_name', 'business_registration_number',)
    list_filter = ('is_new', 'is_approved',)
    search_fields = ('store__name', 'representative_name', 'business_registration_number',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'partner', 'content', 'created_at',)
    list_display_links = ('id', 'store', 'partner', 'content',)
    list_filter = ('partner',)
    search_fields = ('store__name',)