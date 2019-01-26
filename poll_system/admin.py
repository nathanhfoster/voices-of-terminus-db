from django.contrib import admin
from .models import Poll, PollQuestion, PollChoice, PollResponse, PollRecipient

admin.site.register(Poll)
admin.site.register(PollQuestion)
admin.site.register(PollChoice)
admin.site.register(PollResponse)
admin.site.register(PollRecipient)
