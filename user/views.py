from .models import User
from rest_framework import generics
from .serializers import UserSerializer

class UserMixin:
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
 
 
class UserList(UserMixin, generics.ListCreateAPIView):
    """
    Returns list of all Users or create a new User
    """
    # def update_profile(request, user_id):
    #     user = User.objects.get(pk=user_id)
    #     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    #     user.save()
    # pass
 
 
class UserDetails(UserMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a specific User, updates it or deletes it.
    """
    pass