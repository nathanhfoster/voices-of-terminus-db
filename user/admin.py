from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'username', 'id', 'opt_in',
        'primary_race', 'primary_role', 'primary_class', 'secondary_race', 'secondary_role', 'secondary_class',
        'profession', 'profession_specialization',
        'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
        'is_senior_member', 'is_junior_member', 'is_recruit',
        'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
        'can_create_article', 'can_create_newsletter', 'can_create_calendar_event', 'can_create_galleries',
        'can_read_article', 'can_read_newsletter', 'can_read_calendar_event',
        'can_update_article', 'can_update_newsletter', 'can_update_calendar_event',
        'can_delete_article', 'can_delete_newsletter', 'can_delete_calendar_event',
        'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',)


admin.site.register(User, CustomUserAdmin)
