from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500
from .views import *


app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("results/", results, name="results"),
    path("<pk>/comments/",comments, name="comments" ),
    path("signup/", Signup.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
    path("edit_profile/", Edit_profile.as_view(), name="edit_profile"),
    path('addpost/', NewPostView.as_view(), name="addpost"),
    path('<str:pk>', public_profile, name='public_profile'),
]

handler400 = "search.views.handler400"
# handler500 = "search.views.handler500"