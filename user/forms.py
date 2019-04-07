from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = (
            'username', 'id', 'opt_in',
            'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
            'is_senior_member', 'is_junior_member', 'is_recruit',
            'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
            'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username', 'opt_in',
            'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
            'is_senior_member', 'is_junior_member', 'is_recruit',
            'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
            'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',)
