from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from accounts.models import Partner
from stores.models import Store
from partners.models import BusinessRegistration, Feedback
from clients.models import Review


class RegisterBusinessRegistration(serializers.ModelSerializer):
    store_id = serializers.IntegerField()
    # registration_image = serializers.ImageField()

    class Meta:
        model = BusinessRegistration
        fields = ('store_id', 'company_name', 'business_registration_number',
                  'representative_name', 'business_address')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user is None:
                raise serializers.ValidationError("존재하지 않는 User입니다.")
        partner = Partner.objects.get(user=user)
        store = Store.objects.get(pk=validated_data['store_id'])
        store.partner = partner
        store.save()
        
        registration = BusinessRegistration.objects.create(
            store=store,
            partner=partner,
            company_name=validated_data['company_name'],
            business_registration_number=validated_data['business_registration_number'],
            representative_name=validated_data['representative_name'],
            business_address=validated_data['business_address'],
            # registration_image=validated_data['registration_image']
        )
        return registration


# class FeedbackSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Feedback
#         fields = '__all__'
#         read_only_fields = ('id', 'store', 'review', 'partner', 'created_at')

#     def create(self, validated_data):
#         store_id = self.context.get('view').kwargs.get('store_id')
#         if store_id is None:
#             raise serializers.ValidationError("해당 Store가 존재하지 않습니다.")
#         store = Store.objects.get(pk=store_id)
        
#         review_id = self.context.get('view').kwargs.get('review_id')
#         if review_id is None:
#             raise serializers.ValidationError("해당 Review가 존재하지 않습니다.")
#         review = Review.objects.get(pk=review_id)

#         request = self.context.get("request")
#         if request and hasattr(request, "user"):
#             user = request.user
#             if user is None:
#                 raise serializers.ValidationError("존재하지 않는 User입니다.")
#         partner = Partner.objects.get(user=user)

#         feedback = Feedback.objects.create(
#             store=store,
#             review=review,
#             partner=partner,
#             content=validated_data['content']
#         )
#         return feedback