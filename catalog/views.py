from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

# ✅ الصفحة الرئيسية
def home(request):
    products = Product.objects.filter(in_stock=True)  # ✅ عرض المنتجات المتوفرة فقط
    return render(request, 'home.html', {'products': products})


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'catalog/login.html')


# ✅ تسجيل حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        from django.contrib.auth.models import User
        User.objects.create_user(username=username, email=email, password=password)

        return redirect('/')
    return render(request, 'catalog/register.html')


# ✅ من نحن
def about(request):
    return render(request, 'catalog/about.html')


# ✅ ملف المستخدم
@login_required
def profile(request):
    return render(request, 'catalog/profile.html')


# ✅ عرض محتوى السلة
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'catalog/cart_detail.html', {
        'cart': cart,
        'items': cart.items.all(),
        'total': cart.total()
    })


# ✅ إضافة منتج إلى السلة
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')
