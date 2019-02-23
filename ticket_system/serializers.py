from rest_framework import serializers
from ticket_system.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'author', 'author_username',
                  'offender', 'offender_username',
                  'corroborator', 'corroborator_username',
                  'others_involved', 'description',
                  'ticket_type', 'image', 'priority', 'status', 'notes',
                  'date_created', 'last_modified',
                  'date_resolved', 'judge', 'judge_username',
                  'escalated', 'viewed', 'person_who_viewed', 'person_who_viewed_username',
                  )
        read_only_fields = ('id', 'date_created',)
