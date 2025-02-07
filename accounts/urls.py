from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    # path("login/", views.user_login, name="user_login"),
    # path("logout/", views.user_logout, name="user_logout"),
    path("login/", auth_views.LoginView.as_view(), name="user_login"),
    path("logout/", auth_views.LogoutView.as_view(), name="user_logout"),
    path("register/", views.register, name="register"),
]
