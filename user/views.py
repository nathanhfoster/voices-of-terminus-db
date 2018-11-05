from rest_framework.permissions import AllowAny

from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from user.permissions import IsUpdateProfile, IsStaffOrTargetUser


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):

        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(UserView, self).get_permissions()
