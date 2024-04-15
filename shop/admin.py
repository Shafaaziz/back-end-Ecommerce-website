from django.contrib import admin
from .models import *
import admin_thumbnails

class CategoryAdmin(admin.ModelAdmin):
    def زمان_ایحاد(self,obj):
        return obj.created_at.strftime('%H:%M %Y/%m/%d')
    def آخرین_تغییر(self,obj):
        return obj.updated_at.strftime('%H:%M %Y/%m/%d')
    list_display = ('name','زمان_ایحاد','آخرین_تغییر')
    search_fields = ('name',)
    prepopulated_fields = {
        'slug':('name',)
    }
class Sub_CategoryAdmin(admin.ModelAdmin): 
    def زمان_ایحاد(self,obj):
        return obj.created_at.strftime('%H:%M %Y/%m/%d')
    def آخرین_تغییر(self,obj):
        return obj.updated_at.strftime('%H:%M %Y/%m/%d')
    list_display = ('name','category','زمان_ایحاد','آخرین_تغییر')
    search_fields = ('name',)
    list_filter = ('category',)
    prepopulated_fields = {
        'slug':('name',)
    }

class VariantInlines(admin.TabularInline):
    model = Variant
    extra = 2

@admin_thumbnails.thumbnail('image')
class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    def زمان_ایجاد(self,obj):
        return obj.created_at.strftime('%H:%M %Y/%m/%d')
    def آخرین_تغییر(self,obj):
        return obj.updated_at.strftime('%H:%M %Y/%m/%d')
    list_display = ('name','amount','price','discount','total_price','زمان_ایجاد','آخرین_تغییر','available',)
    list_filter = ('available','category')
    list_editable = ('amount',)
    search_fields = ('name',)
    inlines = [VariantInlines,ImageGalleryInline]

class CommentAdmin(admin.ModelAdmin):
    def زمان_ایجاد(self,obj):
        return obj.created_at.strftime('%H:%M %Y/%m/%d')
    def آخرین_تغییر(self,obj):
        return obj.updated_at.strftime('%H:%M %Y/%m/%d')
    list_display = ('user','زمان_ایجاد','rate')


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,Sub_CategoryAdmin)
admin.site.register(Variant)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ImageGallery)