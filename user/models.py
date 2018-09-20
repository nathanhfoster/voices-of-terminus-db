from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(null=True, blank=True)

    discord_url = models.CharField(null=True, blank=True, max_length=250)
    twitter_url = models.CharField(null=True, blank=True, max_length=250)
    twitch_url = models.CharField(null=True, blank=True, max_length=250)
    youtube_url = models.CharField(null=True, blank=True, max_length=250)

    primary_class = models.CharField(null=True, blank=True, max_length=20)
    primary_role = models.CharField(null=True, blank=True, max_length=20)
    secondary_class = models.CharField(null=True, blank=True, max_length=20)
    secondary_role = models.CharField(null=True, blank=True, max_length=20)

    pass