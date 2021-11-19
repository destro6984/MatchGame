from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.core.validators import MaxValueValidator
from django.forms import ModelForm, TextInput
from datetime import date

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', max_length=100)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditUserForm(ModelForm):
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}),
                                 validators=[MaxValueValidator(limit_value=date.today().strftime('%Y-%m-%d'),
                                                               message="Future Date")])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'username', 'avatar']
