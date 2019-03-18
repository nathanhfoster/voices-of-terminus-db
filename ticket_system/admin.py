from django.contrib import admin
from .models import Ticket, Note, StatusChange

admin.site.register(Ticket)
admin.site.register(Note)
admin.site.register(StatusChange)