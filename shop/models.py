from django.db import models
from django.urls import reverse
from account.models import *
from django.forms import ModelForm
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django_jalali.db import models as jmodels


class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='نام' ,unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True,null=True,blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True,verbose_name='آخرین تغییر')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', args=[self.slug,self.id])

class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub',verbose_name='ریز دسته بندی')
    name = models.CharField(max_length=40,unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True,null=True,blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True,verbose_name='آخرین تغییر')

    class Meta:
        verbose_name = 'ریز دسته بندی' 
        verbose_name_plural = 'ریز دسته بندی‌ها'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('sub_category', args=[self.slug,self.id])
    
class Product(models.Model):
    VARIANT = (
        ('سایز','سایز'),
        ('رنگ','رنگ'),
    )

    category = models.ManyToManyField(Sub_Category,verbose_name='دسته بندی')
    name = models.CharField(max_length=50,verbose_name='نام')
    amount = models.IntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveIntegerField(verbose_name='تخفیف',blank=True,null=True)
    total_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')
    information = RichTextField(blank=True,null=True,verbose_name='جزئیات محصول')
    image = models.ImageField(upload_to='product/',verbose_name='عکس')
    status = models.CharField(null=True,blank=True,max_length=50,choices=VARIANT)
    available = models.BooleanField(default=True,verbose_name='موجودی')
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    updated_at = jmodels.jDateTimeField(auto_now=True,verbose_name='آخرین تغییر')
    tags = TaggableManager(blank=True)
    like = models.ManyToManyField(User,blank=True,related_name='product_like')
    total_like = models.IntegerField(default=0)
    unlike = models.ManyToManyField(User,blank=True,related_name='product_unlike')
    total_unlike = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return str(self.name)
    
    @property
    def total_price(self):
        if not self.discount: 
            return self.price
        elif self.discount:
            total = (self.discount * self.price) / 100
            return int(self.price - total)
        return self.total_price
    def total_like(self):
        return self.like.count()
    def total_unlike(self):
        return self.unlike.count()
    
    # def available(self):
    #     if self.amount == 0:
    #         return self.available == True
    #     else:
    #         return self.available == False

class Size(models.Model):
    name = models.CharField(max_length=3,verbose_name='سایز')

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز'
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=40, verbose_name='نام رنگ')

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ‌ها'
    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'نام')
    product_variant = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name= 'محصول')
    size_variant = models.OneToOneField(Size,on_delete=models.CASCADE,null=True,blank=True,verbose_name= 'سایز')
    color_variant = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True, verbose_name= 'رنگ')
    amount = models.IntegerField(verbose_name= 'تعداد')
    price = models.PositiveIntegerField(verbose_name= 'قیمت')
    discount = models.PositiveIntegerField(blank=True,null=True, verbose_name= 'تخفیف')
    total_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')

    class Meta:
        verbose_name = 'تنوع'
        verbose_name_plural = 'تنوع'

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        if not self.discount: 
            return self.price
        elif self.discount:
            total = (self.discount * self.price) / 100
            return int(self.price - total)
        return self.total_price
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default=1)
    create_at = jmodels.jDateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='comment_reply')
    is_reply = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'نطر'
        verbose_name_plural = 'نظرها'

    def __str__(self):
        return str(self.product.name)
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','rate']

class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]

class ImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='product/',blank=True,null=True)

    class Meta:
        verbose_name = 'گالری عکس‌ها'
        verbose_name_plural = 'گالری عکس‌ها'
    
    def __str__(self):
        return self.product.name
