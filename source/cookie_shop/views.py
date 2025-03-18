from django.shortcuts import render


def index(request):
    return render(request, "cookie_shop/index.html", context={"prenom": "Alex"})