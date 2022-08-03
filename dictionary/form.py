from dataclasses import fields
from django.contrib.auth.views import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm, SetPasswordForm
from .models import *

User = get_user_model()


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "username")
        field_classes = {"username": UsernameField}


# class User_change(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ("__all__")

class User_change(SetPasswordForm):
        old_password = forms.CharField(
        label=("Old password"),
        strip=True,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password"}
        ),
    )
        class Meta:
            model= User
            fields=("old_password", "new_password1", "new_password2")