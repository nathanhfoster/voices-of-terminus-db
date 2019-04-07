from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from user.models import User, Character, Setting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('date_joined',)

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            profile_image=validated_data['profile_image'],
            opt_in=validated_data['opt_in']
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    # def create_user(self, username, email, password=None):
    #     if username is None:
    #         raise TypeError('Users must have a username.')

    #     if email is None:
    #         raise TypeError('Users must have an email address.')

    #     user = User(email=validated_data['email'], username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    # def restore_object(self, attrs, instance=None):
    #     # call set_password on user object. Without this
    #     # the password will be stored in plain text.
    #     user = super(UserSerializer, self).restore_object(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'author', 'author_username', 'name',
                  'level', 'race', 'role', 'character_class', 'profession', 'profession_specialization', 'main', 'alt', 'date_created', 'last_modified',)
        read_only_fields = ('id',)


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ('id', 'user', 'show_footer', 'push_messages',)
        read_only_fields = ('id',)


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'groups', 'user_permissions',
            'is_superuser', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
            'is_senior_member', 'is_junior_member', 'is_recruit',
            'is_raid_leader', 'is_banker', 'is_recruiter',
            'is_class_lead', 'is_crafter_lead', 'is_host', 'is_lore_master',
            'is_active', 'experience_points', 'guild_points', 'last_login',
        )


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'groups', 'user_permissions', 'username', 'first_name', 'last_name', 'opt_in', 'lfg', 'last_login',
            'bio', 'is_superuser', 'email', 'is_staff', 'is_leader', 'is_advisor', 'is_council', 'is_general_officer', 'is_officer',
            'is_senior_member', 'is_junior_member', 'is_recruit',
            'is_raid_leader', 'is_banker', 'is_recruiter',
            'is_class_lead', 'is_crafter_lead', 'is_host', 'is_lore_master',
            'is_active', 'date_joined', 'last_login', 'experience_points', 'guild_points',
            'discord_url', 'twitter_url', 'twitch_url', 'youtube_url',
        )
