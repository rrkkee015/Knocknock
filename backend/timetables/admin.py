from django.contrib import admin
from timetables.models import (
    BusinessHour,
    PublicHoliday,
    HolidayHour,
    Dayoff
)

@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ('store', 'day', 'is_dayoff', 'start', 'end', 'start_break', 'end_break', 'last_order',)
    list_display_links = ('store', 'day',)
    list_filter = ('day', 'is_dayoff',)
    search_fields = ('store__name',)

@admin.register(PublicHoliday)
class PublicHolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_display_links = ('name', 'date',)
    search_fields = ('name',)

@admin.register(HolidayHour)
class HolidayHourAdmin(admin.ModelAdmin):
    list_display = ('store', 'public_holiday', 'is_dayoff', 'start', 'end', 'start_break', 'end_break', 'last_order',)
    list_display_links = ('store', 'public_holiday',)
    list_filter = ('public_holiday__name', 'is_dayoff',)
    search_fields = ('store__name',)

@admin.register(Dayoff)
class DayoffAdmin(admin.ModelAdmin):
    pass
