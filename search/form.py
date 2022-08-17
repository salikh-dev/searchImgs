from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from django.contrib.auth.views import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from .models import *
from django.contrib.auth.views import LoginView
User = get_user_model()


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "username")
        field_classes = {"username": UsernameField}

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("img","img_title", "author")
        widgets = {
            'img_title':forms.TextInput(attrs={"class": "form-control","placeholder":"Post title"})
        }
class User_change(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('cust_user','img', "bio")
        # widgets = {'bio': forms.CharField(attrs={"class":"form-control", "placeholder": "enter your bio"})
        # }


