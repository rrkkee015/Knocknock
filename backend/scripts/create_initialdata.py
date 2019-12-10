import csv
import json

from stores.models import Category, Option, Store
from menus.models import Menu


def run():
    with open('/Users/dylan/Desktop/github/s1p1151009/backend/init_data/seoul_stores.csv', 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        fields = ['id', 'name', 'businessCategory', 'category', 'desc', 'x', 'y', 'imageSrc', 'phone',
                  'roadAddr', 'commonAddr', 'addr', 'tags', 'options', 'totalReviewCount', 'priceCategory', 'menus']
        for idx, row in enumerate(reader):
            if idx and idx % 10000 == 0:
                print(f'{idx}개 음식점 완료!')
            origin_id = row['id']
            name = row['name']
            description = row['description']
            if Category.objects.filter(sub_category=row['subCategory']).exists():
                category = Category.objects.get(
                    sub_category=row['subCategory'])
            else:
                if row['subCategory'] == '카페':
                    main_category = '카페'
                else:
                    main_category = '음식점'
                category = Category.objects.create(
                    main_category=main_category, sub_category=row['subCategory'])
            lon = row['x']
            lat = row['y']
            location = f'SRID=4326;POINT ({lon} {lat})'
            thumbnail = row['imageSrc']
            contact = row['phone']
            road_addr = row['roadAddr']
            common_addr = row['commonAddr']
            addr = row['addr']
            if row['priceCategory']:
                price_avg = int(row['priceCategory'].split('만원 대')[0] + '0000')
            else:
                price_avg = 0

            if row['totalReviewCount']:
                review_cnt = int(''.join(row['totalReviewCount'].split(',')))
            else:
                review_cnt = 0
            if row['tags']:
                tags = ','.join([tag for tag in eval(row['tags'])])
            else:
                tags = ''
            store = Store.objects.create(origin_id=origin_id, name=name, category=category, description=description, location=location,
                                         lon=lon, lat=lat, thumbnail=thumbnail, contact=contact, road_addr=road_addr, common_addr=common_addr,
                                         addr=addr, tags=tags, price_avg=price_avg, review_cnt=review_cnt)
            for option in row['options'].split(','):
                if not option.strip():
                    continue
                if Option.objects.filter(name=option).exists():
                    opt = Option.objects.get(name=option)
                else:
                    opt = Option.objects.create(name=option)
                store.options.add(opt)

            store.save()

            if row['menus'].strip():
                for menu in eval(row['menus']):
                    try:
                        name = menu['name']
                        thumbnail = menu['images'][0] if menu['images'] else ''
                        price = int(menu['price'])
                        description = menu['description'] if menu['description'] else ''
                    except:
                        continue

                    Menu.objects.create(
                        store=store,
                        name=name,
                        thumbnail=thumbnail,
                        price=price,
                        description=description
                    )
