from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime

class MyUser(AbstractUser):
    img = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)

   

class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    img = models.ImageField()
    img_title = models.CharField(max_length=150)
    creat_time = models.DateField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.img_title
