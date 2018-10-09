from rest_framework import serializers

from newsletter.models import NewsLetter
from django.contrib.auth.models import User

class NewsLetterSerializer(serializers.ModelSerializer):
    #author_name = serializers.StringRelatedField(source='author_name')
    #author_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = NewsLetter
        fields = ('id','title', 'slug', 'author', 'html', 'tags', 'design',
        'date_created', 'date_modified','last_modified', 'last_modified_by',
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')