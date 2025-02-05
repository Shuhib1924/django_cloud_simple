from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return HttpResponse("logged in")
        else:
            return HttpResponse("user not found")
    else:
        return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("cloud:index")
