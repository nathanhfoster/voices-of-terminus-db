from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title, self.body, self.date_created, self.date_modified)