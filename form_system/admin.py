from django.contrib import admin
from .models import Form, FormQuestion, FormChoice, FormResponse, FormRecipient

admin.site.register(Form)
admin.site.register(FormQuestion)
admin.site.register(FormChoice)
admin.site.register(FormResponse)
admin.site.register(FormRecipient)
