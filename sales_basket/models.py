from django.db import models
from shop.models import *
from django.forms import ModelForm

class Sales(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE,null=True,blank=True,verbose_name='تنوع')
    quantity = models.PositiveIntegerField(verbose_name='تعداد',default=1)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'

    def __str__(self):
        return self.user.username

class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['quantity',]