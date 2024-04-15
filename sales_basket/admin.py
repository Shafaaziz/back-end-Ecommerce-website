from django.contrib import admin
from . models import *

class SalesAdmin(admin.ModelAdmin):
    list_display = ('user','product','variant','quantity')


admin.site.register(Sales,SalesAdmin)