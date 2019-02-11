from rest_framework import serializers
from guild_calendar.models import Event, EventGroup, EventGroupMember


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'start_date', 'end_date', 'title', 'description',
                  'author', 'author_username', 'tags', 'min_level', 'max_level', 'location', 'group_size',
                  'date_created', 'date_modified', 'last_modified', 'last_modified_by', 'last_modified_by_username',
                  )
        read_only_fields = ('id', 'date_created',)


class EventGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGroup
        fields = ('id', 'event_id', 'position',)
        read_only_fields = ('id',)


class EventGroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGroupMember
        fields = ('id', 'event_group_id', 'position',
                  'role_class_preferences', )
        read_only_fields = ('id',)
