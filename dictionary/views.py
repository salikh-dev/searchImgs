from django.shortcuts import render, reverse
from .models import *
from .form import *
from django.views import generic


def home(request):
    imges = UploadImg.objects.all()
    return render(request, 'home.html', {"vid":imges})

def results(request):
    serfun = request.GET.get("search", "")
    if serfun and serfun != "":
        img = UploadImg.objects.filter(img_title__contains=serfun).all()
    else:
        img = ''

    context = {
        "video":img,
        "value":serfun
        }
    
    return render(request, "results.html", context)

def fullscreen(request, pk):
    img = UploadImg.objects.get(id=pk)
    return render(request,"fullscreen.html", {"img":img})

class Signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUp
    def get_success_url(self):
        return reverse("app:home")
    
    
class Profile(generic.TemplateView):
    template_name = "profile/profile.html"