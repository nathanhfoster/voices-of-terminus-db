from rest_framework.permissions import AllowAny
from django.db.models import F
from rest_framework import serializers

from .models import User, Character, Setting
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CharacterSerializer, SettingSerializer, Serializer, AdminSerializer
from user.permissions import IsUpdateProfile, IsStaffOrTargetUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from django.contrib.auth.models import update_last_login


class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(CharacterView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        queryset = Character.objects.all().filter(author=pk)

        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)


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
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(UserView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def refresh(self, request, pk):
        qs = User.objects.values(
            'is_superuser', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
            'is_senior_member', 'is_junior_member', 'is_recruit',
            'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead', 'is_host',
            'can_create_article', 'can_create_newsletter', 'can_create_calendar_event',
            'can_create_galleries', 'can_create_lore', 'can_create_references',
            'can_read_article', 'can_read_newsletter', 'can_read_calendar_event',
            'can_update_article', 'can_update_newsletter', 'can_update_calendar_event',
            'can_delete_article', 'can_delete_newsletter', 'can_delete_calendar_event',
            'is_active', 'experience_points', 'guild_points', 'opt_in', 'last_login',
        ).get(pk=pk)

        if request.user and request.user.is_authenticated:
            user = request.user
            user.last_login = now()
            user.save(update_fields=['last_login'])

        return Response(Serializer(qs).data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def all(self, request):
        qs = User.objects.all()
        serializer = AdminSerializer(qs, many=True)
        return Response(serializer.data)


class SettingView(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(SettingView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        queryset = Setting.objects.all().filter(user=pk)

        serializer = SettingSerializer(queryset, many=True)

        if serializer.data:
            return Response(serializer.data[0])
        else:
            return Response({'show_footer': False, 'push_messages': False})
