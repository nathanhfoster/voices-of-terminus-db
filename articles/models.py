from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='documentAuthorName',
        on_delete=models.CASCADE,)
    def author_username(self):
        return self.author. get_username()
    author_username.short_description = 'Username' 
    html = models.TextField()
    tags = models.CharField(max_length=128, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='articleModifier',
        on_delete=models.CASCADE,)
    def last_modified_by_username(self):
        return self.last_modified_by. get_username()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-last_modified',)

    
class ArticleComment(models.Model):
    document_id = models.ForeignKey(
        Article,
        related_name='comments',
        null=True,
        on_delete=models.CASCADE,)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,)
    def author_username(self):
        return self.author. get_username()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='articleCommentModifier',
        on_delete=models.CASCADE,)
    def last_modified_by_username(self):
        return self.last_modified_by. get_username()
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'
        ordering = ('-last_modified',)