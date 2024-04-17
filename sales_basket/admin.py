from django.contrib import admin
from . models import *


class SalesAdmin(admin.ModelAdmin):
    list_display = ('user','product','variant','quantity')


class ItemInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user','product','variant','size','quantity']


class OrderAdmin(admin.ModelAdmin):
    def زمان_ایجاد(self,obj):
        return obj.created_at.strftime('%H:%M %Y/%m/%d')
    list_display = ('user','email','first_name','last_name','address','IP_address','زمان_ایجاد','paid')
    inlines = [ItemInline]


admin.site.register(ItemOrder)
admin.site.register(Order,OrderAdmin)
admin.site.register(Sales,SalesAdmin)