from django.db import models
from django.conf import settings


class Event(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='eventAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()
    tags = models.CharField(max_length=128, default='Event')
    min_level = models.PositiveIntegerField(default=1)
    max_level = models.PositiveIntegerField(default=60)
    role_preferences = models.CharField(blank=True, null=True, max_length=256)
    class_preferences = models.CharField(blank=True, null=True, max_length=256)
    location = models.CharField(blank=True, null=True, max_length=256)
    congregation_size = models.PositiveIntegerField(default=6)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
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
