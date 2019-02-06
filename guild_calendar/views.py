from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        return super(EventView, self).get_permissions()

    @action(methods=['post'], detail=False)
    def view(self, request):
        dateString = request.data['date']
        date = dateString.split('-')
        year = date[0]
        month = date[1]
        day = date[2].split('T')[0]

        # print(dateString)
        # print(year, month, day)

        queryset = Event.objects.all().filter(
            start_date__year__gte=year,
            start_date__month__gte=month,
            end_date__year__lte=year,
            end_date__month__lte=month, )

        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
