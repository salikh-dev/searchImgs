from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass
    


class Profile(models.Model):
    img = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)
    facebook = models.CharField(max_length=70, null=True, blank=True)
    telegram = models.CharField(max_length=70, null=True, blank=True)
    instagram = models.CharField(max_length=70, null=True, blank=True)
    pinterest = models.CharField(max_length=70, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user



class UploadImg(models.Model):
    img_title = models.CharField(max_length=150)
    img = models.FileField()

    def __str__(self):
        return self.img_title
