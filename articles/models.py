from django.db import models
from django.conf import settings

class Document(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='documentAuthorName',
        on_delete=models.CASCADE,)
    html = models.TextField()
    tags = models.CharField(max_length=128, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='documentModifier',
        on_delete=models.CASCADE,)
    
    # def __str__(self):
    #     """Return a human readable representation of the model instance."""
    #     return "{}".format(
    #         self.title, self.slug, self.author,
    #         self.body, self.tags,
    #         self.date_created, self.date_modified,
    #         self.last_modified, self.last_modified_by)