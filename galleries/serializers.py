from rest_framework import serializers
from galleries.models import Gallery, GalleryImages
from django.contrib.auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'description', 'slug', 'image', 'author', 'author_username', 'tags',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username',
                  )
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')

class GalleryNoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'description', 'slug', 'author', 'author_username', 'tags',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username',
                  )
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'image',)


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ('id', 'title', 'description', 'gallery_id', 'image', 'author', 'author_username',
                  'date_created', 'tags', 'views',)
        read_only_fields = ('date_created',)

class GalleryNoImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ('id', 'title', 'description', 'gallery_id', 'author', 'author_username',
                  'date_created', 'tags', 'views',)
        read_only_fields = ('date_created',)


class GalleryImagesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ('id', 'image',)
