from django.db import models
from django.conf import settings


class Form(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='FormAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    author_username.short_description = 'authorUsername'

    tags = models.CharField(max_length=512, default='Form')
    expiration_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
        ordering = ('-last_modified',)


class FormQuestion(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='FormQuestionAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    question = models.TextField(blank=True, null=True, max_length=280)
    question_type = models.CharField(max_length=28, default="Multiple")
    image = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    form_id = models.ForeignKey(
        Form,
        related_name='FormQuestion',
        on_delete=models.CASCADE,)

    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('position',)


class FormChoice(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='FormChoiceAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    title = models.CharField(blank=True, null=True, max_length=280)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    question_id = models.ForeignKey(
        FormQuestion,
        related_name='FormChoice',
        on_delete=models.CASCADE,)

    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        ordering = ('question_id', 'position',)


class FormResponse(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='FormResponseAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    response = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    choice_id = models.ForeignKey(
        FormChoice,
        related_name='FormResponse',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        ordering = ('id',)
        unique_together = ('author', 'choice_id',)


class FormRecipient(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='FormRecipient',
        null=True,
        on_delete=models.CASCADE,)

    def recipient_username(self):
        return self.recipient. get_username()

    recipient_username.short_description = 'recipientUsername'

    recipient_form_id = models.ForeignKey(
        Form,
        related_name='FormGroup',
        blank=True,
        null=True,
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'
        ordering = ('id',)
