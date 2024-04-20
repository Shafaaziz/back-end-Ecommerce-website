from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django_jalali.db import models as jmodels


class UserManager(BaseUserManager):
    def create_user(self,phone,):
        if not phone:
            raise ValueError('!لطفا شماره همراه خود را وارد کنید')
        user = self.model(phone=phone,)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,phone,password):
        if not email:
            raise ValueError('!لطفا ایمیل خود را وارد کنید')
        if not username:
            raise ValueError('!لطفا نام کاربری خود را وارد کنید')
        if not phone:
            raise ValueError('!لطفا شماره همراه خود را وارد کنید')
        user = self.model(email=self.normalize_email(email),username=username,phone=phone)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50,verbose_name='نام کاربری',null=True,blank=True)
    email = models.EmailField(null=True,blank=True,verbose_name='ایمیل')
    phone = models.CharField(unique=True,max_length=11,verbose_name='شماره همراه')
    address = models.TextField(null=True,blank=True,verbose_name='آدرس')
    IP_address = models.PositiveIntegerField(null=True,blank=True,verbose_name='کد پستی')
    is_active = models.BooleanField(default=True,verbose_name='حساب کاربری فعال')
    is_admin = models.BooleanField(default=False,verbose_name='حساب کاربری ادمین')
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='زمان عضویت')
    updated_at = jmodels.jDateTimeField(auto_now=True,verbose_name='زمان آخرین تغییرات')
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email', ]
    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
         return str(self.username)
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    

