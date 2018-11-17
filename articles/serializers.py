from rest_framework import serializers
from articles.models import Article, ArticleComment
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ('id','document_id', 'author', 'author_username', 'text',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'likes'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')