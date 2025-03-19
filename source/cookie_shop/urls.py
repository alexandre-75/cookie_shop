from django.contrib import admin
from django.urls import  include, path

from .views import index
from products_management.views import product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('produits/', include("products_management.urls")),
    path('produits/<str:slug>', product_detail, name="product_detail"),
    path('users/', include("users_management.urls")),
]
