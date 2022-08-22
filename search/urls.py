from turtle import down
from django.urls import path
from .views import *


app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("results/", results, name="results"),
    path("signup/", Signup.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
    path("edit_profile/", Edit_profile.as_view(), name="edit_profile"),
    path('addpost/', NewPostView.as_view(), name="addpost"),
    path('<str:pk>', public_profile, name='public_profile'),
    path('download/<int:pk>', home, name='download'),
    path('users/', users, name="users"),
]
