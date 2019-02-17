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


class Character(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='characterAuthorName',
        on_delete=models.CASCADE,)

    def author_username(self):
        return self.author. get_username()

    name = models.CharField(blank=True, null=True, max_length=128)
    level = models.PositiveIntegerField(default=1)
    race = models.CharField(blank=True, null=True, max_length=20)
    role = models.CharField(blank=True, null=True, max_length=20)
    character_class = models.CharField(blank=True, null=True, max_length=20)
    profession = models.CharField(blank=True, max_length=20)
    profession_specialization = models.CharField(blank=True, max_length=20)
    main = models.BooleanField(default=False)
    alt = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
        ordering = ('-main', '-alt', '-date_created',)
        # unique_together = ('main', 'author',)


class User(AbstractUser):
    profile_image = models.TextField(blank=True)
    username_validator = MyValidator()
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    bio = models.TextField(blank=True, null=True)
    opt_in = models.BooleanField(blank=True, default=False)
    lfg = models.BooleanField(blank=True, default=False)

    # Connections
    discord_url = models.CharField(blank=True, max_length=250)
    twitter_url = models.CharField(blank=True, max_length=250)
    twitch_url = models.CharField(blank=True, max_length=250)
    youtube_url = models.CharField(blank=True, max_length=250)

    # In game
    experience_points = models.IntegerField(default=0)
    guild_points = models.IntegerField(default=0)

    # Roles
    is_leader = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
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
    can_create_galleries = models.BooleanField(default=False)

    can_read_article = models.BooleanField(default=True)
    can_read_newsletter = models.BooleanField(default=True)
    can_read_calendar_event = models.BooleanField(default=True)

    can_update_article = models.BooleanField(default=False)
    can_update_newsletter = models.BooleanField(default=False)
    can_update_calendar_event = models.BooleanField(default=False)

    can_delete_article = models.BooleanField(default=False)
    can_delete_newsletter = models.BooleanField(default=False)
    can_delete_calendar_event = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-username',)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
    pass

    @property
    def get_profile_image(self):
        return self.profile_image
