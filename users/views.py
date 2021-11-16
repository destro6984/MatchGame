from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from users.forms import LoginForm


class LoginEmailView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_field_name = 'home'
