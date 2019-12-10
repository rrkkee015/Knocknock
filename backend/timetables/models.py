from django.db import models
from stores.models import Store

class BusinessHour(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='business_hours', verbose_name='가게')
    day = models.CharField('요일', max_length=5)
    is_dayoff = models.BooleanField('휴업', default=False)
    start = models.TimeField('영업 시작', null=True, blank=True)
    end = models.TimeField('영업 종료', null=True, blank=True)
    start_break = models.TimeField('브레이크타임 시작', null=True, blank=True)
    end_break = models.TimeField('브레이크타임 종료', null=True, blank=True)
    last_order = models.TimeField('라스트오더', null=True, blank=True)
    memo = models.CharField('비고', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = '영업일 영업시간'
        verbose_name_plural = '영업일 영업시간'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'


class PublicHoliday(models.Model):
    name = models.CharField('명칭', max_length=20)
    date = models.DateField('날짜')

    class Meta:
        verbose_name = '법정 공휴일'
        verbose_name_plural = '법정 공휴일'
        ordering = ['-date']
    
    def __str__(self):
        return f'{self.name}'


class HolidayHour(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='holiday_hours', verbose_name='가게')
    public_holiday = models.ForeignKey(PublicHoliday, on_delete=models.CASCADE, related_name='holiday_hours', verbose_name='명칭')
    is_dayoff = models.BooleanField('휴업', default=False)
    start = models.TimeField('영업 시작', null=True, blank=True)
    end = models.TimeField('영업 종료', null=True, blank=True)
    start_break = models.TimeField('브레이크타임 시작', null=True, blank=True)
    end_break = models.TimeField('브레이크타임 종료', null=True, blank=True)
    last_order = models.TimeField('라스트오더', null=True, blank=True)
    memo = models.CharField('비고', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = '공휴일 영업시간'
        verbose_name_plural = '공휴일 영업시간'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'


class Dayoff(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='dayoffs')
    expiry = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = '휴무일'
        verbose_name_plural = '휴무일'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'
