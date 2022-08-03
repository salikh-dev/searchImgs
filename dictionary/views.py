from django.shortcuts import render, reverse
from .models import *
from .form import *
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm


def home(request):
    imges = UploadImg.objects.all()
    context ={
        "imgpost": imges
        }
    return render(request, 'home.html',context)


def results(request):
    serfun = request.GET.get("search", "")
    if serfun and serfun != "":
        img = UploadImg.objects.filter(img_title__contains=serfun).all()
    else:
        img = ''

    context = {
        "video": img,
        "value": serfun
    }

    return render(request, "results.html", context)


class Signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUp

    def get_success_url(self):
        return reverse("login")


class Profile(generic.TemplateView):
    template_name = "profile/profile.html"


class Edit_profile(generic.UpdateView):
    form_class = User_change
    template_name = "profile/edit_profile.html"
    success_url = reverse_lazy('app:profile')

    def get_object(self):
        return self.request.user
