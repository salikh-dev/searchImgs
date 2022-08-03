from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    img = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)
    


class UploadImg(models.Model):
    img_title = models.CharField(max_length=150)
    img = models.FileField()

    def __str__(self):
        return self.img_title
