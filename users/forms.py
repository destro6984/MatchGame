from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', max_length=100)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
