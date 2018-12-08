from rest_framework import serializers
from galleries.models import Gallery, GalleryImages
from django.contrib.auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'description', 'image', 'slug', 'author', 'author_username', 'author_profile_image', 'tags',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username',
                  )
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ('id', 'title', 'description', 'gallery_id', 'author', 'author_username',
                  'date_created', 'tags', 'views', 'image',)
        read_only_fields = ('date_created',)
