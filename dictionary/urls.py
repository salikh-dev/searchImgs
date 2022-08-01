from django.urls import path
from .views import *


app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("resaults/", results, name="results"),
    path("signup/", Signup.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile")
]