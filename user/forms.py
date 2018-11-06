from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('is_leader', 'is_council', 'is_general_officer', 'is_officer', 'is_senior_member', 'is_junior_member', 'is_recruit')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('is_leader', 'is_council', 'is_general_officer', 'is_officer', 'is_senior_member', 'is_junior_member', 'is_recruit')