from django.db import models
from django.conf import settings


class UserGroup(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='groupAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    author_username.short_description = 'authorUsername'

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    uri = models.CharField(blank=True, null=True, max_length=280)

    @property
    def get_group_title(self):
        return self.title

    @property
    def get_group_author(self):
        return self.author. get_username()

    @property
    def get_last_modified(self):
        return self.last_modified

    @property
    def get_uri(self):
        return self.uri

    class Meta:
        verbose_name = 'UserGroup'
        verbose_name_plural = 'UserGroups'
        ordering = ('-date_created',)


class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='messageAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    body = models.TextField(max_length=280)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    group_message_id = models.ForeignKey(
        UserGroup,
        related_name='groupMessage',
        on_delete=models.CASCADE,)

    @property
    def get_message_body(self):
        return self.body

    @property
    def get_message_last_modified(self):
        return self.last_modified

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-date_created',)


class MessageRecipient(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='messageRecipient',
        null=True,
        on_delete=models.CASCADE,)

    def recipient_username(self):
        return self.recipient. get_username()

    recipient_username.short_description = 'recipientUsername'

    recipient_group_id = models.ForeignKey(
        UserGroup,
        related_name='messageGroup',
        blank=True,
        null=True,
        on_delete=models.CASCADE,)

    # def group_title(self):
    #     return self.recipient_group_id. get_group_title

    # def group_author(self):
    #     return self.recipient_group_id. get_group_author

    # def group_last_modified(self):
    #     return self.recipient_group_id. last_modified

    # def group_uri(self):
    #     return self.recipient_group_id. uri

    message_id = models.ForeignKey(
        Message,
        related_name='message',
        on_delete=models.CASCADE,)

    def message_body(self):
        return self.message_id. get_message_body

    def message_last_modified(self):
        return self.message_id. get_message_last_modified

    is_read = models.BooleanField(default=False)
