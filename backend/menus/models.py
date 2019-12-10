from django.db import models
from stores.models import Store

# Create your models here.
class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='가게', related_name="menus")
    session = models.CharField('세션 이름', max_length=150, blank=True, null=True)
    name = models.CharField('이름', max_length=150)
    thumbnail = models.CharField('썸네일', max_length=1000, blank=True, default='')
    price = models.IntegerField('가격')
    description = models.CharField('설명', max_length=1000, blank=True, default='')

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴'
        ordering = ['id']

    def __str__(self):
        return f'{self.store.name} | {self.name}'
