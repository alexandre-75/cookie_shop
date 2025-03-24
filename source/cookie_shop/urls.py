from django.contrib import admin
from django.urls import  include, path
from .views import about, homepage



urlpatterns = [ 
    path('', homepage, name="homepage"),
    path('a_propos/', about, name="about"),
    path('produits/', include("products.urls")),
    path('panier/', include("shopping_cart.urls")),
    path('compte/', include("accounts.urls")),
    path('admin/', admin.site.urls),
]
