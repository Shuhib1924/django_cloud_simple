from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Profile


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


@login_required
def profile(request):
    profile = get_object_or_404(Profile, user__username=request.user.username)
    # user = get_object_or_404(User, username=username)
    if request.method == "POST":
        # data = request.POST
        # files = request.FILES
        if "date_of_birth" in request.POST:
            profile.date_of_birth = request.POST["date_of_birth"]
        if "photo" in request.FILES:
            profile.photo = request.FILES["photo"]
        profile.save()
        # return redirect("accounts:profile", username=profile.user.username)
        return redirect("accounts:profile")
    else:
        return render(request, "profile.html", {"profile": profile})
