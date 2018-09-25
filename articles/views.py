from .models import Document
from rest_framework import viewsets
from .serializers import DocumentSerializer

class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
