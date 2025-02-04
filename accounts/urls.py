from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
]
