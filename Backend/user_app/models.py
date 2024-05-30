from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


# Create your models here.
def upload_image_path(instance, filename):
    return "/profile/" + str(filename)

class User(AbstractUser):
    nickname = models.CharField(max_length=55)
    profile_picture = ResizedImageField(upload_to='profile_pictures', blank=True, null=True)