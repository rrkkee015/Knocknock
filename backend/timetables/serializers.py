from rest_framework import serializers

from stores.models import Store
from timetables.models import BusinessHour

class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHour
        fields = '__all__'

    def create(self, validated_data):
        store = Store.objects.get(pk=validated_data['store'])

        business_hour = BusinessHour.objects.create(
            store=store,
            day=validated_data['day'],
            is_dayoff=validated_data['is_dayoff'],
            start=validated_data.get('start'),
            end=validated_data.get('end'),
            start_break=validated_data.get('start_break'),
            end_break=validated_data.get('end_break'),
            last_order=validated_data.get('last_order'),
            memo=validated_data.get('memo', '')
        )
        return business_hour

    def update(self, instance, validated_data):
        instance.is_dayoff = validated_data.get('is_dayoff', instance.is_dayoff)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.start_break = validated_data.get('start_break', instance.start_break)
        instance.end_break = validated_data.get('end_break', instance.end_break)
        instance.last_order = validated_data.get('last_order', instance.last_order)
        instance.memo = validated_data.get('memo', instance.memo)
        instance.save()
        return instance