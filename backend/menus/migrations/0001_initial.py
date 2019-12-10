# Generated by Django 2.2.6 on 2019-10-31 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=150, null=True, verbose_name='세션 이름')),
                ('name', models.CharField(max_length=150, verbose_name='이름')),
                ('thumbnail', models.CharField(blank=True, default='', max_length=1000, verbose_name='썸네일')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('description', models.CharField(blank=True, default='', max_length=1000, verbose_name='설명')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='stores.Store', verbose_name='가게')),
            ],
            options={
                'verbose_name': '메뉴',
                'verbose_name_plural': '메뉴',
                'ordering': ['id'],
            },
        ),
    ]
