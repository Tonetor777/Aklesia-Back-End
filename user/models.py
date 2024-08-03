from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile_picture = models.CharField(max_length=50, null=True, blank=True)