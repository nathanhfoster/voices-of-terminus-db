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
                  )
        read_only_fields = ('id', 'date_created',)
