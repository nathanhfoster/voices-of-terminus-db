from django.contrib import admin
from .models import Newsletter, NewsletterLikes, NewsletterComment

admin.site.register(Newsletter)
admin.site.register(NewsletterLikes)
admin.site.register(NewsletterComment)