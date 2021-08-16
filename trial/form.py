from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    email = forms.Emailfield(Required= True)

    class Meta:
        model = User 
        field = ['username', 'email', 'password1', 'password2']