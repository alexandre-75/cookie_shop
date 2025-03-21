from django.urls import path
from shopping_cart.views import add_to_cart
from .views import all_products, product_details


urlpatterns = [
    path('', all_products, name="products-all_products"),
    path('<str:slug>/', product_details, name="products-product_details"), 
    path('<str:slug>/add_to_cart', add_to_cart, name="products-add_to_cart"), # direction view.py de shopping_cart, sans création de template
]