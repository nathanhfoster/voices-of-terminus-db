from .models import Document
from rest_framework import generics
from .serializers import DocumentsSerializer

# Create your views here.
class DocumentsView(generics.ListCreateAPIView):
    """
    generics.ListCreateAPIView => GET, POST, HEAD, OPTIONS
    """
    queryset = Document.objects.all()
    serializer_class = DocumentsSerializer

# class DocumentsView(generics.UpdateAPIView):
#     """
#     generics.UpdateAPIView =>     PUT, PATCH, DELETE, OPTIONS
#     """
#     queryset = Document.objects.all()
#     serializer_class = DocumentsSerializer

# class DocumentsView(generics.DestroyAPIView ):
#     """
#     generics.DestroyAPIView =>    DELETE, OPTIONS
#     """
#     queryset = Document.objects.all()
#     serializer_class = DocumentsSerializer