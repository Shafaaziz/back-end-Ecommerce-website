from django.urls import path
from . import views


app_name = 'sale'
urlpatterns = [
    path('', views.basket_detail, name='sales_basket'),
    path('add/<int:id>/',views.add_basket, name='add_basket'),
    path('remove/<int:id>/',views.remove_basket,name='remove_basket'),
    path('order/<int:order_id>', views.order, name='order'),
    path('create/',views.order_create, name='order_create'),
    path('request/<int:price>',views.send_request,name='request'),
    path('verify/',views.verify, name='verify'),

]