from django.db.models import F
from rest_framework import permissions, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from poll_system.permissions import IsOwnerOrReadOnly, CanUpdateRecipient

from .models import Poll, PollQuestion, PollResponse, PollRecipient
from .serializers import PollSeializer, PollQuestionSeializer, PollResponseSeializer, PollRecipientSeializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PollView(viewsets.ModelViewSet):
    serializer_class = PollSeializer
    pagination_class = StandardResultsSetPagination
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        return super(PollView, self).get_permissions()

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'
        ordering = ('-last_modified',)


class PollQuestionView(viewsets.ModelViewSet):
    serializer_class = PollQuestionSeializer
    pagination_class = LargeResultsSetPagination
    queryset = PollQuestion.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        return super(PollQuestionView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = PollQuestion.objects.all().filter(poll_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PollQuestionSeializer(queryset, many=True)
        return Response(serializer.data)

    class Meta:
        verbose_name = 'PollQuestion'
        verbose_name_plural = 'PollQuestions'
        ordering = ('-id',)


class PollResponseView(viewsets.ModelViewSet):
    serializer_class = PollResponseSeializer
    pagination_class = LargeResultsSetPagination
    queryset = PollResponse.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        return super(PollResponseView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = PollResponse.objects.all().filter(question_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PollResponseSeializer(queryset, many=True)
        return Response(serializer.data)

    class Meta:
        verbose_name = 'PollResponse'
        verbose_name_plural = 'PollResponses'
        ordering = ('-id',)


class PollRecipientView(viewsets.ModelViewSet):
    serializer_class = PollRecipientSeializer
    pagination_class = LargeResultsSetPagination
    queryset = PollRecipient.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, CanUpdateRecipient,)
        return super(PollRecipientView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = PollRecipient.objects.all().filter(recipient=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PollRecipientSeializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PollRecipientSeializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def poll(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        # .distinct('recipient')
        queryset = PollRecipient.objects.all().filter(
            recipient_poll_id=pk).values('recipient_id').distinct()

        # newlist = []
        # for i in queryset:
        #     print(i)
        #     if i.recipient_id not in newlist:
        #         newlist.append(i.recipient_id)

        # print(newlist)

        serializer = PollRecipientSeializer(queryset, many=True)
        return Response(serializer.data)

    class Meta:
        verbose_name = 'PollRecipient'
        verbose_name_plural = 'PollRecipients'
        ordering = ('-id',)
