from django.db import models
from django.conf import settings


class Gallery(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=250, null=True)
    image = models.TextField(blank=True)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='galleryAuthorName',
        on_delete=models.CASCADE,)

    def author_username(self):
        return self.author. get_username()

    def author_profile_image(self):
        return self.author. get_profile_image
    author_username.short_description = 'Username'
    tags = models.CharField(max_length=128, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='galleryModifier',
        on_delete=models.CASCADE,)

    def last_modified_by_username(self):
        return self.last_modified_by. get_username()

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ('-last_modified',)


class GalleryImages(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=250, null=True)
    gallery_id = models.ForeignKey(
        Gallery,
        related_name='galleryImages',
        null=True,
        on_delete=models.CASCADE,)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)

    def author_username(self):
        return self.author. get_username()
    author_username.short_description = 'Username'
    tags = models.CharField(max_length=128, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='galleryImageModifier',
        on_delete=models.CASCADE,)

    def last_modified_by_username(self):
        return self.last_modified_by. get_username()
    views = models.PositiveIntegerField(default=0)
    image = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
        ordering = ('-date_created',)
