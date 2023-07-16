
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
  class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
   
from .models import Task
class TForm(ModelForm):
    class Meta:
        model = Task
        fields = ['tag','text', 'to_date', 'author','img']
