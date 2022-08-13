from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)
    
    class Meta:
        verbose_name = 'My User'
        verbose_name_plural = 'User'



class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    img = models.ImageField()
    img_title = models.CharField(max_length=150)
    comment = models.TextField(max_length=700)
    creat_time = models.DateField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.img_title



class Followerslen(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user