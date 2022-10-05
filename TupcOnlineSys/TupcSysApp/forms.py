from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import pics, register1


class Registration(UserCreationForm):
    class Meta:
        model= register1    
        fields = ['username', 'first_name', 'last_name', 'email', 'idno', 'password1', 'password2', 'Personal_description']

