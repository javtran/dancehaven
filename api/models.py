from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Profiles
#   name
#   picture/video
#   description
#   location  (city, country)
#   contact
#       email
#   ethnicity
#   gender
#   height
#   age
#   company/studio
#   personal website
#   socials: instagram, tiktok, youtube


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000000, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    ethnicity = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    height = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)


# Crews
#   name
#   description
#   location  (city, country)
#   contact
#       email, phone
#   company/studio
#   personal website
#   socials: instagram, tiktok, youtube

# Performances
#   Videos
#   Description
#   Choreographer
#   Company
#   date
#   Dancers
