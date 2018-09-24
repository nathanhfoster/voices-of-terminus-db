from .models import Document
from rest_framework import generics, viewsets
from .serializers import DocumentSerializer

class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    authentication_classes = ()
    permission_classes = ()