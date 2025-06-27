from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('', views.home, name='catalog_home'),
    path('login/', views.login_view, name='catalog_login'),
    path('register/', register_view, name='register'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart_detail, name='cart_detail'),
]


