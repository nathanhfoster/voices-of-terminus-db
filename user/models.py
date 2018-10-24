from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Allo Spaces in User names
class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'

class User(AbstractUser):
    username_validator = MyValidator()
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text = ('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
            error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(null=True, upload_to='images/profiles')

    discord_url = models.CharField(blank=True, max_length=250)
    twitter_url = models.CharField(blank=True, max_length=250)
    twitch_url = models.CharField(blank=True, max_length=250)
    youtube_url = models.CharField(blank=True, max_length=250)

    primary_race = models.CharField(blank=True, max_length=20)
    primary_role = models.CharField(blank=True, max_length=20)
    primary_class = models.CharField(blank=True, max_length=20)
    
    secondary_race = models.CharField(blank=True, max_length=20)
    secondary_role = models.CharField(blank=True, max_length=20)
    secondary_class = models.CharField(blank=True, max_length=20)
    

    profession = models.CharField(blank=True, max_length=20)
    profession_specialization = models.CharField(blank=True, max_length=20)
    experience_points = models.IntegerField(default=0)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
    pass