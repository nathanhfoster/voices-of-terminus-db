from django.db import models
from django.conf import settings
from user.models import Character
from django.shortcuts import get_object_or_404


class Event(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250)
    url = models.CharField(blank=True, null=True, max_length=1024)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='eventAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    def author_profile_image(self):
        return self.author. get_profile_image
    tags = models.CharField(max_length=128, default='Event')
    min_level = models.PositiveIntegerField(default=1)
    max_level = models.PositiveIntegerField(default=60)
    locations = models.CharField(blank=True, null=True, max_length=256)
    group_size = models.PositiveIntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='eventModifier',
        on_delete=models.CASCADE,)

    def last_modified_by_username(self):
        return self.last_modified_by. get_username()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('date_created',)


class EventGroup(models.Model):
    event_id = models.ForeignKey(
        Event,
        related_name='eventGroup',
        on_delete=models.CASCADE,)
    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'EventGroup'
        verbose_name_plural = 'EventGroups'
        ordering = ('position',)


class EventGroupMember(models.Model):
    event_group_id = models.ForeignKey(
        EventGroup,
        related_name='eventGroupMember',
        on_delete=models.CASCADE,)
    position = models.PositiveIntegerField()
    role_class_preferences = models.TextField(
        blank=True, null=True,)

    filled = models.ForeignKey(
        Character,
        related_name='eventGroupMemberAuthorName',
        on_delete=models.CASCADE,
        blank=True, null=True,)

    class Meta:
        verbose_name = 'EventGroupMember'
        verbose_name_plural = 'EventGroupMembers'
        ordering = ('position',)
