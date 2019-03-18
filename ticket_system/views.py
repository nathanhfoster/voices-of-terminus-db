from .models import Ticket, Note, StatusChange
from rest_framework import viewsets
from .serializers import TicketSerializer, NoteSerializer, StatusChangeSerializer
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
        queryset = Ticket.objects.all().filter(author=pk)

        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)


class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        return super(NoteView, self).get_permissions()

    @action(methods=['get'], detail=True)
    def view(self, request, pk):
        queryset = Note.objects.all().filter(ticket_id=pk)

        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

class StatusChangeView(viewsets.ModelViewSet):
    serializer_class = StatusChangeSerializer
    queryset = StatusChange.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        return super(StatusChangeView, self).get_permissions()

    @action(methods=['get'], detail=True)
    def view(self, request, pk):
        queryset = StatusChange.objects.all().filter(ticket_id=pk)

        serializer = StatusChangeSerializer(queryset, many=True)
        return Response(serializer.data)