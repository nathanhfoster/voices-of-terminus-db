from .models import User
from rest_framework import generics, viewsets
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()