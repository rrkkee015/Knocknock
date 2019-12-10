from django.db import models
from accounts.models import Client
from stores.models import Store

class Review(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='가게', related_name='reviews')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='클라이언트', related_name='reviews')
    content = models.CharField('내용', max_length=300)
    created_at = models.DateTimeField('작성일', auto_now_add=True)

    class Meta:
        verbose_name = '클라이언트 리뷰'
        verbose_name_plural = '클라이언트 리뷰'
        ordering = ['id']

    def __str__(self):
        return f'{self.store.name} | {self.client.nickname} | {self.content}'