from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', max_length=100)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditUserForm(ModelForm):
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'username', 'avatar']
