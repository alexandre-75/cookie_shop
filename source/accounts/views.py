from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render


User = get_user_model()

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  
        return redirect("homepage")
    return render(request, "sign_up.html")

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("homepage")  
    return render(request, "sign_in.html")

def logout_user(request):
    logout(request)
    return redirect("homepage")
