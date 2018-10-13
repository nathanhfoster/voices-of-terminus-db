from .models import Document
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializers import DocumentSerializer
from articles.permissions import IsOwnerOrReadOnly

class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
        return super(DocumentView, self).get_permissions()