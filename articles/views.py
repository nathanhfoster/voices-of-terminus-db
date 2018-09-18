from .models import Document
from rest_framework import generics
from .serializers import DocumentsSerializer

# Create your views here.
class DocumentsView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentsSerializer