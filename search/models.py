from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'My User'
        verbose_name_plural = 'User'


class Profile(models.Model):
    cust_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=70, blank=True)
    img =  models.ImageField(default="userprofile.png", upload_to="profile_pic")


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    img = models.ImageField()
    img_title = models.CharField(max_length=150)
    comment = models.TextField(max_length=700)
    creat_time = models.CharField(default=datetime.now().strftime("%H:%M:%S"))
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.img_title



class Followerslen(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

