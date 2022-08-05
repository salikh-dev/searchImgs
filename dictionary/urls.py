from django.urls import path
from .views import *


app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("resaults/", results, name="results"),
    path("signup/", Signup.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
    path("edit_profile/", Edit_profile.as_view(), name="edit_profile"),
    path('<str:pk>/', public_profile, name='public_profile'),
]

