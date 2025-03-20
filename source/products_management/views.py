from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    context = {
        'extra_css': 'css/all_products.css',
        'products': products,
        }
    return render(request, "all_products.html", context)

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'extra_css':'css/product_details.css',
        'product_details':product,
        }
    return render(request, "product_details.html", context)
    