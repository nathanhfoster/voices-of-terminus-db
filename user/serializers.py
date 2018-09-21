from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author_name')
    class Meta:
        model = User
        fields = (
        'id', 'username', 'password', 'first_name', 'last_name',
        'bio', 'profile_image', 'primary_role', 'secondary_class', 'secondary_role', 
        'last_login', 'is_superuser', 'email', 'is_staff',
        'is_active', 'date_joined',  
        'discord_url', 'twitter_url', 'twitch_url', 'youtube_url',
        'primary_class', )
        extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user