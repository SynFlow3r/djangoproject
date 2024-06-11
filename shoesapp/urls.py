from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_register, name='login'),
    path('profile/', views.profile, name='profile'),
    path('cardpay/', views.card_pay, name='cardpay')
]
