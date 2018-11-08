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
    profile_image = models.TextField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3xpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3MDc4MzNlNi1iY2Q5LTQwYWUtYTZlOC1hMjQ5NTYwNDA2MDMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6M0JGNEQ5QkQ1REY1MTFFNUIwMEFGMUU4MUQ4MjcxNDQiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6M0JGNEQ5QkM1REY1MTFFNUIwMEFGMUU4MUQ4MjcxNDQiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpCQjk0NjBEOUM5NURFNTExQjA0OEM4MUM1OTA5NjlDMSIgc3RSZWY6ZG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjI3Mzg5ZjJiLTlkNWMtMTE3OC04MTdlLWY1M2RhM2Fi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')
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

    # Connections
    discord_url = models.CharField(blank=True, max_length=250)
    twitter_url = models.CharField(blank=True, max_length=250)
    twitch_url = models.CharField(blank=True, max_length=250)
    youtube_url = models.CharField(blank=True, max_length=250)

    # In game
    primary_race = models.CharField(blank=True, max_length=20)
    primary_role = models.CharField(blank=True, max_length=20)
    primary_class = models.CharField(blank=True, max_length=20)
    
    secondary_race = models.CharField(blank=True, max_length=20)
    secondary_role = models.CharField(blank=True, max_length=20)
    secondary_class = models.CharField(blank=True, max_length=20)
    
    profession = models.CharField(blank=True, max_length=20)
    profession_specialization = models.CharField(blank=True, max_length=20)
    experience_points = models.IntegerField(default=0)

    # Roles
    is_leader = models.BooleanField(default=False)
    is_council = models.BooleanField(default=False)
    is_general_officer = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_senior_member = models.BooleanField(default=False)
    is_junior_member = models.BooleanField(default=False)
    is_recruit = models.BooleanField(default=False)

    is_raid_leader = models.BooleanField(default=False)
    is_banker = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    is_class_lead = models.BooleanField(default=False)
    is_crafter_lead = models.BooleanField(default=False)

    # Permissions
    can_create_article = models.BooleanField(default=False)
    can_create_newsletter = models.BooleanField(default=False)
    can_create_calendar_event = models.BooleanField(default=False)

    can_read_article = models.BooleanField(default=True)
    can_read_newsletter = models.BooleanField(default=True)
    can_read_calendar_event = models.BooleanField(default=True)

    can_update_article = models.BooleanField(default=False)
    can_update_newsletter = models.BooleanField(default=False)
    can_update_calendar_event = models.BooleanField(default=False)

    can_delete_article = models.BooleanField(default=False)
    can_delete_newsletter = models.BooleanField(default=False)
    can_delete_calendar_event = models.BooleanField(default=False)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
    pass