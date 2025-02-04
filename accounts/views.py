from django.http import HttpResponse
from django.shortcuts import render


def user_login(request):
    return HttpResponse("logged in")
