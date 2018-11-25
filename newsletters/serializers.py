from rest_framework import serializers
from newsletters.models import Newsletter, NewsletterLikes, NewsletterComment
from django.contrib.auth.models import User

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id','title', 'slug', 'author', 'author_username', 'author_profile_image', 'html', 'tags', 'design',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')
        
class NewsletterLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterLikes
        fields = ('id','document_id', 'author', 'author_username', 'count', 'date_created',)
        read_only_fields = ('date_created',)

class NewsletterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterComment
        fields = ('id','document_id', 'author', 'author_username', 'author_profile_image', 'text',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'likes'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')