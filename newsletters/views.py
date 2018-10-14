from .models import NewsLetter
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializers import NewsLetterSerializer
from newsletters.permissions import IsOwnerOrReadOnly, IsUpdateProfile

class NewsLetterView(viewsets.ModelViewSet):
    serializer_class = NewsLetterSerializer
    queryset = NewsLetter.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile)
        return super(NewsLetterView, self).get_permissions()