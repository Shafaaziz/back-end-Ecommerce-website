from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.authentication, name='auth'),
    # path('auth_verify',views.auth_verify, name='auth_verify'),
    path('profile', views.Profile, name='profile'),
    path('update_profile', views.update_profile,name='update_profile'),
    
]