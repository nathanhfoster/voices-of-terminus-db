from django.db import models
from django.conf import settings

class NewsLetter(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='newsletterAuthorName',
        on_delete=models.CASCADE,)
    body = models.TextField()
    tags = models.CharField(max_length=128, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='newsletterModifier',
        on_delete=models.CASCADE,)