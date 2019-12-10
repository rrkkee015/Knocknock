from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nickname = models.CharField('닉네임', max_length=20)

    class Meta:
        verbose_name = '클라이언트'
        verbose_name_plural = '클라이언트'
        ordering = ['id']

    def __str__(self):
        return f'{self.user.username}'


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='partner')
    name = models.CharField('이름', max_length=15)
    phone = models.CharField('휴대폰 번호', max_length=15)
    email = models.CharField('이메일', max_length=30)

    class Meta:
        verbose_name = '파트너'
        verbose_name_plural = '파트너'
        ordering = ['id']

    def __str__(self):
        return f'{self.user.username}'
