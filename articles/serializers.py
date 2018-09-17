from rest_framework import serializers

from articles.models import Document

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')