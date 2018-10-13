from rest_framework import serializers
from guildcalendar.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','title', 'slug', 'author', 'event_start_date','event_end_date',
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')