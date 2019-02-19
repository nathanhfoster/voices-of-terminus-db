from .models import Ticket
from rest_framework import viewsets
from .serializers import TicketSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        return super(TicketView, self).get_permissions()

    @action(methods=['get'], detail=True)
    def view(self, request, pk):
        queryset = Ticket.objects.all().filter(offender=pk)

        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)
