from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ هذا هو السطر الناقص

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('checkout/', include('checkout.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('catalog.urls')),
]
