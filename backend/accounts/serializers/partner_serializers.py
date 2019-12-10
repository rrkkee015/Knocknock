from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import Partner
from accounts.serializers.client_serializers import UserSerializer


class PartnerSignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)

    class Meta:
        model = Partner
        fields = ('id', 'username', 'password', 'name', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=True
        )
        partner = Partner.objects.create(
            user=user,
            name=validated_data['name'],
            phone=validated_data['phone'],
            email=validated_data['username'],
        )
        return partner


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=20)
#     password = serializers.CharField(max_length=20)

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         return serializers.ValidationError('등록된 사용자가 아닙니다')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Partner
        fields = '__all__'
