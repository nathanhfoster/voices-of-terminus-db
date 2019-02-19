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

    description = models.TextField()
    ticket_type = models.CharField(max_length=128, default='Report')
    image = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, default='Open')

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ('-last_modified',)
