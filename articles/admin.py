from django.contrib import admin
from .models import Article, ArticleLikes, ArticleComment

admin.site.register(Article)
admin.site.register(ArticleLikes)
admin.site.register(ArticleComment)
