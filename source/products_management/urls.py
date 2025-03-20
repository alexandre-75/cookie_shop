from django.urls import path
from .views import all_products, product_details


urlpatterns = [
    path('', all_products, name="products_management-all_products"),
    path('<str:slug>/', product_details, name="products_management-product_details"),
]