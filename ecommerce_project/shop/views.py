from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

@login_required(login_url='/admin/login/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='/admin/login/')
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})
@login_required(login_url='/admin/login/')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('home')
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    
    
    cart_items.delete()
    
    return render(request, 'shop/success.html', {'total': total})
@login_required(login_url='/admin/login/')
def remove_from_cart(request, id):
    CartItem.objects.filter(id=id, user=request.user).delete()
    return redirect('cart')
@login_required(login_url='/admin/login/')
def increase_quantity(request, id):
    item = CartItem.objects.get(id=id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

@login_required(login_url='/admin/login/')
def decrease_quantity(request, id):
    item = CartItem.objects.get(id=id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')
def logout_view(request):
    logout(request)
    return redirect('home')
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'shop/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'shop/register.html')