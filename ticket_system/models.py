from django.db import models
from django.conf import settings


class Ticket(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='ticketAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    offender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='ticketOffenderName',
        on_delete=models.CASCADE, blank=True, null=True)

    def offender_username(self):
        try:
            return self.offender. get_username()
        except:
            return None

    corroborator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='corroboratorAuthorName',
        on_delete=models.CASCADE, blank=True, null=True)

    def corroborator_username(self):
        try:
            return self.corroborator. get_username()
        except:
            return None
    others_involved = models.CharField(max_length=1024, blank=True, null=True)

    description = models.TextField()
    ticket_type = models.CharField(max_length=128, default='Report')
    image = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, default='Open')

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_resolved = models.DateTimeField(blank=True, null=True)

    judge = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='judgeAuthorName',
        on_delete=models.CASCADE, blank=True, null=True)

    def judge_username(self):
        try:
            return self.judge. get_username()
        except:
            return None

    escalated = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    person_who_viewed = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='personWhoViewedAuthorName',
        on_delete=models.CASCADE, blank=True, null=True)

    def person_who_viewed_username(self):
        try:
            return self.person_who_viewed. get_username()
        except:
            return None

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ('status', '-priority',)


class StatusChange(models.Model):
    ticket_id = models.ForeignKey(
        Ticket,
        related_name='statusChanges',
        on_delete=models.PROTECT, )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='statusChangeAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Open')

    class Meta:
        verbose_name = 'StatusChange'
        verbose_name_plural = 'StatusChanges'
        ordering = ('-date_created',)


class Note(models.Model):
    ticket_id = models.ForeignKey(
        Ticket,
        related_name='ticketNotes',
        on_delete=models.PROTECT, )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='noteAuthorName',
        on_delete=models.CASCADE, )

    def author_username(self):
        try:
            return self.author. get_username()
        except:
            return None

    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ('-date_created',)


# class PersonInvolved(models.Model):
#     ticket_id = models.ForeignKey(
#         Ticket,
#         related_name='ticketId',
#         on_delete=models.PROTECT, )
#     person = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name='personInvolvedAuthorName',
#         on_delete=models.CASCADE, )

#     def person_username(self):
#         try:
#             return self.person. get_username()
#         except:
#             return None

#     someone = models.CharField(max_length=128, blank=True, null=True)
