from products.models import Product, ProductCategory
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'active': True,
    }

    return render(request, "products/products.html", context)
