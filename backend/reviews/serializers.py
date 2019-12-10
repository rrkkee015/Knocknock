from rest_framework import serializers
from accounts.models import Client
from accounts.serializers.client_serializers import ClientSerializer
from feedbacks.serializers import FeedbackSerializer
from stores.models import Store
from clients.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField('get_store_name')
    client = serializers.StringRelatedField(read_only=True)
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'client', 'created_at', 'store_name',)

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
            
        review = Review.objects.create(
            store=validated_data['store'],
            client=Client.objects.get(user=user),
            content=validated_data['content']
        )
        return review
    
    def get_store_name(self, obj):
        return obj.store.name