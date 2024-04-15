from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('account/',include('account.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sales_basket/', include('sales_basket.urls',namespace= 'sale')),
]
