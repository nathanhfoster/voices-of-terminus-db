from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
