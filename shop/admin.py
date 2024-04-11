from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
    search_fields = ('name',)
    prepopulated_fields = {
        'slug':('name',)
    }
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category','created_at','updated_at')
    search_fields = ('name',)
    list_filter = ('category',)
    prepopulated_fields = {
        'slug':('name',)
    }

class VariantInlines(admin.TabularInline):
    model = Variant
    extra = 2

class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','amount','price','discount','total_price','created_at','updated_at','available',)
    list_filter = ('available','category')
    list_editable = ('amount',)
    search_fields = ('name',)
    inlines = [VariantInlines,ImageGalleryInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','create_at','rate')


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,Sub_CategoryAdmin)
admin.site.register(Variant)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ImageGallery)