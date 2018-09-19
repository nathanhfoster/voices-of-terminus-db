from rest_framework import serializers

from articles.models import Document
from django.contrib.auth.models import User

class DocumentsSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author_name')
    class Meta:
        model = Document
        fields = ('id','title', 'slug', 'author', 'body', 'tags',
        'date_created', 'date_modified','last_modified', 'last_modified_by')
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')