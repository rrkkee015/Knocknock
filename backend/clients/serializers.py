from rest_framework import serializers
from accounts.models import Client
from accounts.serializers.client_serializers import ClientSerializer
from partners.serializers import FeedbackSerializer
from stores.models import Store
from clients.models import Review


# class ReviewSerializer(serializers.ModelSerializer):
#     client = serializers.StringRelatedField(read_only=True)
#     feedbacks = FeedbackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('id', 'client', 'store', 'created_at')

#     def create(self, validated_data):
#         store_id = self.context.get('view').kwargs.get('store_id')
#         if store_id is None:
#             raise serializers.ValidationError("해당 Store가 존재하지 않습니다.")
        
#         request = self.context.get("request")
#         if request and hasattr(request, "user"):
#             user = request.user
#             if user is None:
#                 raise serializers.ValidationError("존재하지 않는 User입니다.")
#         client = Client.objects.get(user=user)
#         store = Store.objects.get(pk=store_id)
#         review = Review.objects.create(
#             store=store,
#             client=client,
#             content=validated_data['content']
#         )
#         return review