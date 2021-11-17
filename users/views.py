from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import LoginForm, SignUpForm
from users.models import User


# SuccessMessageMixin


class LoginEmailView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_field_name = 'home'
    # success_message=f'Welcome'


class LogoutView(auth_views.LogoutView):
    template_name = "users/logout.html"


class SingUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'users/registration_form.html'
