from rest_framework import serializers

from newsletters.models import NewsLetter
from django.contrib.auth.models import User

class NewsLetterSerializer(serializers.ModelSerializer):
    #author_name = serializers.StringRelatedField(source='author_name')
    #author_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = NewsLetter
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags', 'design',
        'date_created', 'date_modified','last_modified', 'last_modified_by', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')