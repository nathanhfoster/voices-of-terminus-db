from rest_framework import serializers
from poll_system.models import Poll, PollQuestion, PollResponse, PollRecipient
from django.contrib.auth.models import User


class PollSeializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'author', 'author_username',
                  'date_created', 'last_modified', )
        read_only_fields = ('id', 'date_created', )


class PollQuestionSeializer(serializers.ModelSerializer):
    class Meta:
        model = PollQuestion
        fields = ('id', 'author', 'author_username', 'question', 'question_type',
                  'date_created', 'last_modified', 'poll_id',
                  )
        read_only_fields = ('id', 'date_created',)


class PollResponseSeializer(serializers.ModelSerializer):
    class Meta:
        model = PollResponse
        fields = ('id', 'author', 'author_username', 'response',
                  'date_created', 'last_modified',
                  'question_id', )
        read_only_fields = ('id',)


class PollRecipientSeializer(serializers.ModelSerializer):
    class Meta:
        model = PollRecipient
        fields = ('id', 'recipient',
                  'recipient_username', 'recipient_poll_id',)
        read_only_fields = ('id',)
