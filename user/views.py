from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()