from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Character, Setting


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'username', 'id', 'opt_in',
        'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
        'is_senior_member', 'is_junior_member', 'is_recruit',
        'is_raid_leader', 'is_banker', 'is_recruiter', 'is_class_lead', 'is_crafter_lead',
        'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Character)
admin.site.register(Setting)
