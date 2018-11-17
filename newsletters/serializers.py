from rest_framework import serializers
from newsletters.models import Newsletter, NewsletterComment
from django.contrib.auth.models import User

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags', 'design',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')

class NewsletterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterComment
        fields = ('id','document_id', 'author', 'author_username', 'text',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'likes'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')