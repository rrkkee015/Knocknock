from rest_framework import serializers

from accounts.models import Partner, Client
from accounts.serializers.client_serializers import ClientSerializer
from stores.models import Category, Option, Store
from reviews.serializers import ReviewSerializer
from menus.serializers import MenuSerializer
from timetables.models import BusinessHour
from timetables.serializers import BusinessHourSerializer

from datetime import datetime, timedelta


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('main_category', 'sub_category',)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name',)


class StoreByDistanceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    distance = serializers.SerializerMethodField('get_distance')
    left_time = serializers.SerializerMethodField('get_left_minutes')

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'price_avg', 'distance', 'left_time',)

    def get_distance(self, obj):
        return int(obj.distance.m)

    def convert_minute(self, a, b):
        _to = datetime.strptime(a.strftime('%H:%M'), '%H:%M')
        _from = datetime.strptime(b.strftime('%H:%M'), '%H:%M')
        return (_from - _to).seconds // 60

    def get_left_minutes(self, obj):
        day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        today = datetime.now().weekday()
        time = datetime.strptime(
            datetime.now().strftime('%H:%M'), '%H:%M').time()
        bhours = BusinessHour.objects.filter(store=obj)
        today_business = bhours.get(day=day[today])
        yesterday_business = bhours.get(day=day[today-1])
        if time < today_business.start:
            if today_business.start == today_business.end:
                return -1

        if today_business.is_dayoff == False:
            if today_business.start < today_business.end:
                if today_business.start_break:
                    if time < today_business.start_break:
                        return self.convert_minute(time, today_business.start_break)
                    else:
                        if today_business.last_order:
                            if time < today_business.last_order:
                                return self.convert_minute(time, today_business.last_order)
                            else:
                                return self.convert_minute(time, today_business.end)
                        else:
                            return self.convert_minute(time, today_business.end)
                elif today_business.last_order:
                    if time < today_business.last_order:
                        return self.convert_minute(time, today_business.last_order)
                    else:
                        return self.convert_minute(time, today_business.end)
                else:
                    return self.convert_minute(time, today_business.end)
            elif today_business.start == today_business.end:
                return -1
            else:
                if today_business.start_break:
                    if time < today_business.start_break:
                        return self.convert_minute(time, today_business.start_break)
                    else:
                        if today_business.last_order:
                            if time < today_business.last_order:
                                return self.convert_minute(time, today_business.last_order)
                            else:
                                return self.convert_minute(time, today_business.end)
                        else:
                            return self.convert_minute(time, today_business.end)
                elif today_business.last_order:
                    if time < today_business.last_order:
                        return self.convert_minute(time, today_business.last_order)
                    else:
                        return self.convert_minute(time, today_business.end)
                else:
                    return self.convert_minute(time, today_business.end)
        else:
            if yesterday_business.start == yesterday_business.end:
                return -1
            else:
                if yesterday_business.start_break:
                    if time < yesterday_business.start_break:
                        return self.convert_minute(time, yesterday_business.start_break)
                    else:
                        if yesterday_business.last_order:
                            if time < yesterday_business.last_order:
                                return self.convert_minute(time, yesterday_business.last_order)
                            else:
                                return self.convert_minute(time, yesterday_business.end)
                        else:
                            return self.convert_minute(time, yesterday_business.end)
                elif yesterday_business.last_order:
                    if time < yesterday_business.last_order:
                        return self.convert_minute(time, yesterday_business.last_order)
                    else:
                        return self.convert_minute(time, yesterday_business.end)
                else:
                    return self.convert_minute(time, yesterday_business.end)


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'lon', 'lat', 'thumbnail', 'contact', 'road_addr',
                  'common_addr', 'addr', 'view_cnt',)


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    options = serializers.StringRelatedField(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)
    business_hours = BusinessHourSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'category', 'description', 'lon', 'lat', 'thumbnail', 'contact',
                  'road_addr', 'common_addr', 'addr', 'tags', 'price_avg', 'partner', 'review_cnt',
                  'view_cnt', 'menus', 'reviews', 'options', 'business_hours',)
