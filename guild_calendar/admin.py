from django.contrib import admin
from .models import Event, EventGroup, EventGroupMember

admin.site.register(Event)
admin.site.register(EventGroup)
admin.site.register(EventGroupMember)
