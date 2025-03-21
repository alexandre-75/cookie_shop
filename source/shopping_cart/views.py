from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from shopping_cart.models import Cart, CartItem

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    item, created = CartItem.objects.get_or_create(user=user, product=product)
    if created:
        cart.items.add(item)
        cart.save()
    else:
        item.quantity += 1
        item.save()
    return redirect('products-all_products')

def cart(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    return render(request, 'cart.html', context={'cart': cart.items.all()})

def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.items.all().delete()
        cart.delete()
    return redirect('products-all_products')
    