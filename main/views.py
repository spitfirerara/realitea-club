import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.utils.html import strip_tags
from .forms import ProductForm
from .models import Product
from django.contrib import messages

# Views halaman biasa

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406433112',
        'name': request.user.username,
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

#  JSON / API endpoints untuk AJAX
def _product_to_dict(prod: Product):
    return {
        'id': str(prod.id),
        'name': prod.name,
        'price': prod.price,
        'description': prod.description,
        'thumbnail': prod.thumbnail or '',
        'category': prod.category,
        'is_featured': prod.is_featured,
        'stock': prod.stock,
        'brand': prod.brand or '',
        'user_id': prod.user.id if prod.user else None,
        'created_at': prod.created_at.isoformat() if prod.created_at else None,
        'updated_at': prod.updated_at.isoformat() if prod.updated_at else None,
    }

def show_json(request):
    product_list = Product.objects.order_by('-created_at').all()
    data = [_product_to_dict(p) for p in product_list]
    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        return JsonResponse(_product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

# AJAX Create (POST)

@login_required(login_url='/login')
@require_POST
def add_product_ajax(request):
    # Sanitasi input
    name = strip_tags(request.POST.get('name', '')).strip()
    description = strip_tags(request.POST.get('description', '')).strip()
    price = request.POST.get('price') or 0
    thumbnail = request.POST.get('thumbnail', '').strip()
    category = request.POST.get('category', '').strip()

    if not name:
        return JsonResponse({'detail': 'Name required'}, status=400)

    try:
        price_int = int(price)
    except:
        price_int = 0

    product = Product.objects.create(
        user=request.user,
        name=name,
        price=price_int,
        description=description,
        thumbnail=thumbnail,
        category=category
    )

    return JsonResponse(_product_to_dict(product), status=201)

# AJAX Edit (POST)

@login_required(login_url='/login')
@require_POST
def edit_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.user != request.user:
        return JsonResponse({'detail': 'Forbidden'}, status=403)

    name = strip_tags(request.POST.get('name', '')).strip()
    description = strip_tags(request.POST.get('description', '')).strip()
    price = request.POST.get('price') or 0
    thumbnail = request.POST.get('thumbnail', '').strip()
    category = request.POST.get('category', '').strip()

    try:
        price_int = int(price)
    except:
        price_int = product.price

    if name:
        product.name = name
    product.description = description
    product.price = price_int
    product.thumbnail = thumbnail
    product.category = category
    product.save()

    return JsonResponse(_product_to_dict(product))

# AJAX Delete (POST)

@login_required(login_url='/login')
@require_POST
def delete_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user != request.user:
        return JsonResponse({'detail': 'Forbidden'}, status=403)
    product.delete()
    return JsonResponse({'detail': 'deleted'}, status=204)

# Auth 
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
   try:
    product = Product.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product)
    return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

# TI 4   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('main:login')
        else:
            messages.error(request, 'Failed to register. Please check the form.')
    
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, f'Welcome back, {user.username}!')
            return response
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# category views
from django.shortcuts import render
def jersey(request):
    products = Product.objects.filter(category="jersey")
    return render(request, "category.html", {"products": products, "category": "Jersey"})

def shoes(request):
    products = Product.objects.filter(category="shoes")
    return render(request, "category.html", {"products": products, "category": "Shoes"})

def ball(request):
    products = Product.objects.filter(category="ball")
    return render(request, "category.html", {"products": products, "category": "Ball"})

def accessory(request):
    products = Product.objects.filter(category="accessory")
    return render(request, "category.html", {"products": products, "category": "Accessory"})

def other(request):
    products = Product.objects.filter(category="other")
    return render(request, "category.html", {"products": products, "category": "Other"})
