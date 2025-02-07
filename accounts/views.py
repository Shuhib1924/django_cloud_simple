from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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


def register(request):
    if request.method == "POST":
        data = request.POST
        # print(f"data: {data}")
        if data["password"] == data["confirm_password"]:
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            login(request, user)
            return redirect("cloud:index")
        else:
            return HttpResponse("passwords don't match")
    return render(request, "registration/register.html")
