from django.contrib import admin
from django.urls import  include, path
from .views import homepage



urlpatterns = [ 
    path('', homepage, name="homepage"),
    path('produits/', include("products_management.urls")),
    path('compte/', include("accounts.urls")),
    path('admin/', admin.site.urls),
]
