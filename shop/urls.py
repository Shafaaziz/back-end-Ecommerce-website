from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('category/<slug>/<int:id>/',views.product, name='category'),
    path('sub_category/<slug>/<int:id>',views.product, name='sub_category'),
    path('like/<int:id>', views.productLike, name='product_like'),
    path('unlike/<int:id>', views.productUnlike, name='product_unlike'),
    path('comment/<int:id>/', views.product_comment, name='product_comment'),
    path('reply/<int:id>/<int:comment_id>',views.comment_reply, name='comment_reply'),
    path('search/', views.product_search, name='product_search')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)