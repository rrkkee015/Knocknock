# Generated by Django 2.2.6 on 2019-10-31 08:33

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(max_length=30, verbose_name='대분류')),
                ('sub_category', models.CharField(max_length=30, verbose_name='중분류')),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='옵션명')),
            ],
            options={
                'verbose_name': '옵션',
                'verbose_name_plural': '옵션',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_id', models.CharField(max_length=20, unique=True, verbose_name='네이버 아이디')),
                ('name', models.CharField(max_length=150, verbose_name='이름')),
                ('description', models.TextField(blank=True, default='', verbose_name='설명')),
                ('lon', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='경도')),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='위도')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='위치')),
                ('thumbnail', models.TextField(blank=True, default='', verbose_name='대표 사진')),
                ('contact', models.CharField(blank=True, default='', max_length=15, verbose_name='전화번호')),
                ('road_addr', models.CharField(blank=True, max_length=150, verbose_name='도로명 주소')),
                ('common_addr', models.CharField(max_length=150, verbose_name='시구')),
                ('addr', models.CharField(blank=True, max_length=150, verbose_name='지번 주소')),
                ('tags', models.TextField(blank=True, default='', verbose_name='태그')),
                ('price_avg', models.IntegerField(default=0, verbose_name='가격대')),
                ('review_cnt', models.IntegerField(default=0, verbose_name='네이버 리뷰갯수')),
                ('view_cnt', models.IntegerField(default=0, verbose_name='조회수')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stores.Category', verbose_name='카테고리')),
                ('options', models.ManyToManyField(blank=True, to='stores.Option', verbose_name='옵션')),
                ('partner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Partner', verbose_name='파트너')),
            ],
            options={
                'verbose_name': '가게',
                'verbose_name_plural': '가게',
                'ordering': ['id'],
            },
        ),
    ]
