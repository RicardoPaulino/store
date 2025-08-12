
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("store:store")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, "store/login.html")

def logout_view(request):
    logout(request)
    return redirect("store:login")
   
@login_required(login_url='store:login') # type: ignore
def store_view(request):
    return render(request, 'store/index.html')
