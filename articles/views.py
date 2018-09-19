from .models import Document
from rest_framework import generics
from .serializers import DocumentsSerializer

#Use for inheritance
class DocumentMixin:
    serializer_class = DocumentsSerializer
    queryset = Document.objects.all()
 
 
class DocumentList(DocumentMixin, generics.ListCreateAPIView):
    """
    Returns list of all Documents or create a new Document
    """
    pass
 
 
class DocumentDetails(DocumentMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a specific Document, updates it or deletes it.
    """
    pass