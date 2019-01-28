from django.db import models
from django.conf import settings


class Poll(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pollAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    author_username.short_description = 'authorUsername'

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'
        ordering = ('-last_modified',)


class PollQuestion(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pollQuestionAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    question = models.TextField(max_length=280)
    question_type = models.CharField(max_length=28, default="Multiple")

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    poll_id = models.ForeignKey(
        Poll,
        related_name='pollQuestion',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('id',)


class PollChoice(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='PollChoiceAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    title = models.CharField(blank=True, null=True, max_length=280)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    question_id = models.ForeignKey(
        PollQuestion,
        related_name='PollChoice',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        ordering = ('id',)


class PollResponse(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='PollResponseAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        return self.author. get_username()

    response = models.CharField(blank=True, null=True, max_length=280)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    choice_id = models.ForeignKey(
        PollChoice,
        related_name='PollResponse',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        ordering = ('id',)
        unique_together = ('author', 'choice_id',)


class PollRecipient(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pollRecipient',
        null=True,
        on_delete=models.CASCADE,)

    def recipient_username(self):
        return self.recipient. get_username()

    recipient_username.short_description = 'recipientUsername'

    recipient_poll_id = models.ForeignKey(
        Poll,
        related_name='pollGroup',
        blank=True,
        null=True,
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'
        ordering = ('id',)
