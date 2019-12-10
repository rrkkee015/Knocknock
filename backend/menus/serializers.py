from rest_framework import serializers

from stores.models import Store
from menus.models import Menu


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        menu = Menu.objects.create(
            store=validated_data.get('store'),
            name=validated_data.get('name'),
            thumbnail=validated_data.get('thumbnail', ''),
            price=validated_data.get('price'),
            description=validated_data.get('description', '')
        )
        return menu