from rest_framework.permissions import AllowAny
from django.db.models import F
from rest_framework import serializers

from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from user.permissions import IsUpdateProfile, IsStaffOrTargetUser
from rest_framework.decorators import action
from rest_framework.response import Response
import logging


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

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def refresh(self, request, pk):
        qs = User.objects.values(
        'primary_race', 'primary_role', 'primary_class', 'secondary_race', 'secondary_role', 'secondary_class',
        'profession', 'profession_specialization',
        'is_superuser', 'is_staff', 'is_leader', 'is_advisor', 'is_council','is_general_officer', 'is_officer',
        'is_senior_member', 'is_junior_member', 'is_recruit',
        'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
        'can_create_article', 'can_create_newsletter', 'can_create_calendar_event', 'can_create_galleries',
        'can_read_article', 'can_read_newsletter', 'can_read_calendar_event',
        'can_update_article', 'can_update_newsletter', 'can_update_calendar_event',
        'can_delete_article', 'can_delete_newsletter', 'can_delete_calendar_event',
        'is_active', 'experience_points', 'guild_points', 'opt_in'
        ).get(pk=pk)

        return Response(Serializer(qs).data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def all(self, request):
        qs = User.objects.all()
        serializer = AdminSerializer(qs, many=True)
        return Response(serializer.data)

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'primary_race', 'primary_role', 'primary_class', 'secondary_race', 'secondary_role', 'secondary_class',
        'profession', 'profession_specialization',
        'is_superuser', 'is_staff', 'is_leader', 'is_advisor', 'is_council','is_general_officer', 'is_officer',
        'is_senior_member', 'is_junior_member', 'is_recruit',
        'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
        'can_create_article', 'can_create_newsletter', 'can_create_calendar_event', 'can_create_galleries',
        'can_read_article', 'can_read_newsletter', 'can_read_calendar_event',
        'can_update_article', 'can_update_newsletter', 'can_update_calendar_event',
        'can_delete_article', 'can_delete_newsletter', 'can_delete_calendar_event',
        'is_active', 'experience_points', 'guild_points'
        )

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'username', 'first_name', 'last_name', 'opt_in',
        'bio', 'primary_race', 'primary_role', 'primary_class', 'secondary_race', 'secondary_role', 'secondary_class',
        'profession', 'profession_specialization',
        'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council','is_general_officer', 'is_officer',
        'is_senior_member', 'is_junior_member', 'is_recruit',
        'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
        'can_create_article', 'can_create_newsletter', 'can_create_calendar_event', 'can_create_galleries',
        'can_read_article', 'can_read_newsletter', 'can_read_calendar_event',
        'can_update_article', 'can_update_newsletter', 'can_update_calendar_event',
        'can_delete_article', 'can_delete_newsletter', 'can_delete_calendar_event',
        'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',
        'discord_url', 'twitter_url', 'twitch_url', 'youtube_url',
        'primary_class'
        )