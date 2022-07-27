from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class UploadImg(models.Model):
    img_title = models.CharField(max_length=150)
    img = models.FileField()
    def __str__(self):
        return self.img_title

