from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ✅ الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')  # أو 'catalog/home.html' حسب موقع القالب

# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # ✅ توجيه للصفحة الرئيسية
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'catalog/login.html')


def register_view(request):
    if request.method == 'POST':
        # يمكنك لاحقًا استخدام نموذج تسجيل من django.forms
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # التسجيل الفعلي - لاحقًا نستخدم User.objects.create_user()
        print(username, email)  # فقط للعرض حالياً
        return redirect('/')  # يرجع للرئيسية بعد التسجيل
    return render(request, 'catalog/register.html')



def about(request):
    return render(request, 'catalog/about.html')




@login_required
def profile(request):
    return render(request, 'catalog/profile.html')