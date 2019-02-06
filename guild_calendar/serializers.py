from rest_framework import serializers
from guild_calendar.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'start_date', 'end_date', 'title', 'description',
                  'author', 'author_username', 'tags', 'min_level', 'max_level',
                  'role_preferences', 'class_preferences', 'location', 'congregation_size',
                  'date_created', 'date_modified', 'last_modified', 'last_modified_by', 'last_modified_by_username',
                  )
        read_only_fields = ('date_created',)
