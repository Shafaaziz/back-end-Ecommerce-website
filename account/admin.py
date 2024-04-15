from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreateForm
from django.contrib.auth.models import Group
from .models import User
from django_jalali.admin.filters import JDateFieldListFilter

class UserAdmin(BaseUserAdmin):
    change_form = UserChangeForm
    create_form = UserCreateForm
    def admin_create(self,obj):
        return obj.created_at.strftime('%Y/%m/%d %H:%M')
    def admin_update(self,obj):
        return obj.updated_at.strftime('%Y/%m/%d %H:%M')
    list_display = ('username','email','phone','admin_create','admin_update','is_active','is_admin')
    list_filter = ('username','is_admin',('created_at',JDateFieldListFilter))
    fieldsets = (
        ('کاربر',{'fields':('username','email','phone','password')}),
        ('آدرس',{'fields':('address','IP_address')}),
        ('دسترسی‌ها',{'fields':('is_active','is_admin')}),
    )

    add_fieldsets = (
        (None , {'fields':('username','email','phone','password1','password2')}),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
