from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)   
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'isActive': user.is_active,
            'LastLogin': user.last_login,
            'isSuperUser': user.is_superuser,
            'isStaff': user.is_staff,
            'bio': user.bio,
            'primaryRole': user.primary_role,
            'primaryClass': user.primary_class,
            'secondaryRole': user.secondary_class,
            'secondaryClass': user.secondary_role,
            'profession': user.profession,
            'professionSpecialization': user.profession_specialization,
            'dateJoined': user.date_joined,
            'discordUrl': user.discord_url,
            'twitterUrl': user.twitter_url,
            'twitchUrl': user.twitch_url,
            'youtubeUrl': user.youtube_url,
            'experiencePoints': user.experience_points
        })

        

# class TokenAuthenticationView(ObtainAuthToken):
#     """Implementation of ObtainAuthToken with last_login update"""

#     def post(self, request):
#         result = super(TokenAuthenticationView, self).post(request)
#         try:
#             request_user, data = requests.get_parameters(request)
#             user = requests.get_user_by_username(data['username'])
#             update_last_login(None, user)            
#         except Exception as exc:
#             return None
#         return result