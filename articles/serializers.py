from rest_framework import serializers
from articles.models import Document
from django.contrib.auth.models import User

class DocumentSerializer(serializers.ModelSerializer):
    # author_name = serializers.StringRelatedField(source='documentAuthorName')
    #author_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Document
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags',
        'date_created', 'date_modified','last_modified', 'last_modified_by',
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')