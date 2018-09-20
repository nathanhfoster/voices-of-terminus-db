from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author_name')
    class Meta:
        model = Account
        fields = (
        'id', 'password', 'last_login', 'is_superuser',
        'username', 'first_name', 'email', 'is_staff',
        'is_active', 'date_joined', 'last_name', 'bio',
        'profile_image', 'discord_url', 'twitter_url', 'twitch_url', 'youtube_url',
        'primary_class', 'primary_role', 'secondary_class', 'secondary_role')
        # read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')