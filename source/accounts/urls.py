from django.urls import path
from .views import logout_user, sign_in, sign_up

urlpatterns = [
    path("inscription", sign_up, name="accounts-sign_up"),
    path("connexion", sign_in, name="accounts-sign_in"),
    path("deconnexion", logout_user, name="accounts-logout"),
]