from stores.models import Store
from timetables.models import BusinessHour
import csv
import re


def run():
    time_format = re.compile('[\d]{2}:[\d]{2}')

    with open('/Users/dylan/Desktop/github/s1p1151009/backend/init_data/seoul_stores_BusinessHour.csv', 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        file_fields = ['store', 'day', 'is_dayoff', 'start_time',
                       'end_time', 'start_break', 'end_break', 'last_order', 'memo']
        model_fields = ['store', 'day', 'is_dayoff', 'start',
                        'end', 'start_break', 'end_break', 'last_order', 'memo']
        for idx, row in enumerate(reader):
            if idx and idx % 10000 == 0:
                print(f'{idx}개 음식점 완료!')
            store = Store.objects.get(origin_id=row['store'])
            day = row['day']
            is_dayoff = row['is_dayoff']
            memo = row['memo']
            if is_dayoff == 'True':
                BusinessHour.objects.create(
                    store=store,
                    day=day,
                    is_dayoff=is_dayoff,
                    start=None,
                    end=None,
                    start_break=None,
                    end_break=None,
                    last_order=None,
                    memo=memo
                )
            else:
                for key in ['start_time', 'end_time', 'start_break', 'end_break', 'last_order']:
                    if time_format.match(row[key]):
                        if row[key] > '24:00':
                            hour, minute = map(int, row[key].split(':'))
                            hour -= 24
                            row[key] = f'{hour}:{minute}'
                        elif row[key] == '24:00':
                            row[key] = '00:00'
                    else:
                        row[key] = None
                BusinessHour.objects.create(
                    store=store,
                    day=day,
                    is_dayoff=is_dayoff,
                    start=row['start_time'],
                    end=row['end_time'],
                    start_break=row['start_break'],
                    end_break=row['end_break'],
                    last_order=row['last_order'],
                    memo=memo
                )
