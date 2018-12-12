from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='eventAuthorName',
        on_delete=models.CASCADE, )
    event_start_date = models.DateTimeField(auto_now_add=False)
    event_end_date = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='eventModifier',
        on_delete=models.CASCADE,)