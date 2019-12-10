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
            name='PublicHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='명칭')),
                ('date', models.DateField(verbose_name='날짜')),
            ],
            options={
                'verbose_name': '법정 공휴일',
                'verbose_name_plural': '법정 공휴일',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='HolidayHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_dayoff', models.BooleanField(default=False, verbose_name='휴업')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='영업 시작')),
                ('end', models.TimeField(blank=True, null=True, verbose_name='영업 종료')),
                ('start_break', models.TimeField(blank=True, null=True, verbose_name='브레이크타임 시작')),
                ('end_break', models.TimeField(blank=True, null=True, verbose_name='브레이크타임 종료')),
                ('last_order', models.TimeField(blank=True, null=True, verbose_name='라스트오더')),
                ('memo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='비고')),
                ('public_holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holiday_hours', to='timetables.PublicHoliday', verbose_name='명칭')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holiday_hours', to='stores.Store', verbose_name='가게')),
            ],
            options={
                'verbose_name': '공휴일 영업시간',
                'verbose_name_plural': '공휴일 영업시간',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dayoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayoffs', to='stores.Store')),
            ],
            options={
                'verbose_name': '휴무일',
                'verbose_name_plural': '휴무일',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=5, verbose_name='요일')),
                ('is_dayoff', models.BooleanField(default=False, verbose_name='휴업')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='영업 시작')),
                ('end', models.TimeField(blank=True, null=True, verbose_name='영업 종료')),
                ('start_break', models.TimeField(blank=True, null=True, verbose_name='브레이크타임 시작')),
                ('end_break', models.TimeField(blank=True, null=True, verbose_name='브레이크타임 종료')),
                ('last_order', models.TimeField(blank=True, null=True, verbose_name='라스트오더')),
                ('memo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='비고')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_hours', to='stores.Store', verbose_name='가게')),
            ],
            options={
                'verbose_name': '영업일 영업시간',
                'verbose_name_plural': '영업일 영업시간',
                'ordering': ['id'],
            },
        ),
    ]