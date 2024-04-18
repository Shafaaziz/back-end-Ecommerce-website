from django.db import models
from shop.models import *
from django.forms import ModelForm
from account.models import User
from django_jalali.db import models as jmodels
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

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    first_name = models.CharField(max_length=200,verbose_name= 'نام گیرنده')
    last_name = models.CharField(max_length=200,verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11,verbose_name='شماره همراه')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(max_length=1000,verbose_name='آدرس')
    IP_address = models.PositiveIntegerField(verbose_name='کد پستی')
    paid = models.BooleanField(default=False,verbose_name='پرداخت شد؟')
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')


    def __str__(self):
        return self.user.username
    
    def get_price(self):
        total = sum(i.price() for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total
    

    
class ItemOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سفارش',related_name='order_item')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    variant = models.ForeignKey(Variant,on_delete=models.CASCADE,verbose_name='تنوع')
    quantity = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.user.username
    
    def size(self):
        return self.variant.size_variant.name
    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['user','paid','created_at']
    # fields = ['username','phone','email','first_name','last_name','address','IP_address']