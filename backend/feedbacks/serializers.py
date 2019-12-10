from rest_framework import serializers

from accounts.models import Partner
from stores.models import Store
from partners.models import Feedback
from clients.models import Review


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('id', 'store', 'partner', 'created_at')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
        partner = Partner.objects.get(user=user)
        store = Store.objects.get(reviews=validated_data.get('review'))
        feedback = Feedback.objects.create(
            store=store,
            review=validated_data.get('review'),
            partner=partner,
            content=validated_data['content']
        )
        return feedback