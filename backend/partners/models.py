from django.db import models
from accounts.models import Partner
from stores.models import Store
from clients.models import Review


class BusinessRegistration(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='가게')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='파트너')
    is_new = models.BooleanField('신규등록', default=False)
    is_approved = models.BooleanField('승인 여부', default=False)
    company_name = models.CharField('상호', max_length=100)
    business_registration_number = models.CharField('등록번호', max_length=10)
    representative_name = models.CharField('대표자명', max_length=30)
    business_address = models.CharField('업장소재지', max_length=100)
    # registration_image = models.ImageField('사업자 등록증', upload_to='partners/certificates')
    business_commencement_date = models.DateField('영업개시일', null=True)
    business_type = models.CharField('업태', max_length=30, null=True)
    business_item = models.CharField('종목', max_length=30, null=True)

    class Meta:
        verbose_name = '사업자등록증'
        verbose_name_plural = '사업자등록증'
        ordering = ['id']

    def __str__(self):
        return f'{self.company_name} | {self.partner.name}'


class Feedback(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='가게', related_name='feedbacks')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name='답글', related_name='feedbacks')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='파트너', related_name='feedbacks')
    content = models.CharField('내용', max_length=300)
    created_at = models.DateTimeField('작성일', auto_now_add=True)

    class Meta:
        verbose_name = '파드너 피드백'
        verbose_name_plural = '파트너 피드백'
        ordering = ['id']

    def __str__(self):
        return f'{self.store.name} | {self.review.id} | {self.content}'