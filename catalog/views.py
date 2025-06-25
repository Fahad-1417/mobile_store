from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # أو 'catalog/home.html' لو كان داخل مجلد catalog


def login_view(request):
    return render(request, 'catalog/login.html')