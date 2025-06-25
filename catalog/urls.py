from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalog_home'),
    path('login/', views.login_view, name='catalog_login'),
]


