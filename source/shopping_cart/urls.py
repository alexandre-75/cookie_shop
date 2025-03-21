from django.urls import path
from .views import cart, delete_cart


urlpatterns = [
    path('', cart, name="shopping_cart-cart"),
    path('delete', delete_cart, name="shopping_cart-delete_cart"),
    
]
