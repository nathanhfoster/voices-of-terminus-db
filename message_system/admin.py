from django.contrib import admin
from .models import UserGroup, Message, MessageRecipient

admin.site.register(UserGroup)
admin.site.register(Message)
admin.site.register(MessageRecipient)
