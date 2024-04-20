from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.authentication.as_view(), name='auth'),
    # path('auth_verify',views.auth_verify, name='auth_verify'),
    path('profile', views.Profile, name='profile'),
    path('update_profile/<int:pk>/', views.update_profile.as_view(),name='update_profile'),
    
]