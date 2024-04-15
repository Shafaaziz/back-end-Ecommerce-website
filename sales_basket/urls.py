from django.urls import path
from . import views


app_name = 'sale'
urlpatterns = [
    path('', views.basket_detail, name='sales_basket'),
    path('add/<int:id>/',views.add_basket, name='add_basket'),
    path('remove/<int:id>/',views.remove_basket,name='remove_basket'),
]