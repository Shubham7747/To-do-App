from django import forms
from django.db import models
from django.forms import fields
from App_1.models import Trial 

class Task_form(forms.ModelForm):
    class Meta:
        model = Trial
        fields = ['task', 'done']