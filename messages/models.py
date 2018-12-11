from django.db import models
from django.conf import settings

class Message(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='messageAuthorName',
        on_delete=models.CASCADE,)
    def author_username(self):
        return self.author. get_username()
    def author_profile_image(self):
        return self.author. get_profile_image
    author_username.short_description = 'authorUsername'
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='messageRecipientName',
        on_delete=models.CASCADE,)
    def recipient_username(self):
        return self.recipient. get_username()
    def recipient_profile_image(self):
        return self.recipient. get_profile_image
    recipient_username.short_description = 'recipientUsername'
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='articleModifier',
        on_delete=models.CASCADE,)
    def last_modified_by_username(self):
        return self.last_modified_by. get_username()
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-last_modified',)