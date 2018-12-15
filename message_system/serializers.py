from rest_framework import serializers
from message_system.models import UserGroup, Message, MessageRecipient
from django.contrib.auth.models import User


class UserGroupSeializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('id', 'title', 'author', 'author_username',
                  'date_created', 'last_modified', 'uri', 'is_active',)
        read_only_fields = ('id', 'user', 'username',
                            'date_created', 'last_modified')


class MessageSeializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'author', 'author_username', 'body',
                  'date_created', 'last_modified', 'parent_message_id',
                  )
        read_only_fields = ('id', 'date_created',)


class MessageRecipientSeializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRecipient
        fields = ('id', 'recipient', 'recipient_username', 'is_read',
                  'recipient_group_id',
                  #   'group_author', 'group_title', 'group_last_modified', 'group_uri',
                  'message_id', 'message_body', 'message_last_modified')
        read_only_fields = ('id',)


class MessageRecipientViewSeializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRecipient
        fields = ('id', 'is_read',
                  'recipient_group_id',
                  #   'group_author', 'group_title', 'group_last_modified', 'group_uri',
                  'message_id', 'message_body', 'message_last_modified',)
        read_only_fields = ('id',)


class MessageGroupRecipientsSeializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRecipient
        fields = ('recipient_id', )
        read_only_fields = ('recipient_id',)
