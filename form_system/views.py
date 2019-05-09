from django.db.models import F
from rest_framework import permissions, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from form_system.permissions import IsOwnerOrReadOnly

from .models import Form, FormQuestion, FormChoice, FormResponse, FormRecipient
from .serializers import FormSerializer, FormQuestionSerializer, FormChoiceSerializer, FormResponseSeializer, FormRecipientSeializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FormView(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Form.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(FormView, self).get_permissions()


class FormQuestionView(viewsets.ModelViewSet):
    serializer_class = FormQuestionSerializer
    # pagination_class = LargeResultsSetPagination
    queryset = FormQuestion.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(FormQuestionView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = FormQuestion.objects.all().filter(form_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FormQuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class FormChoiceView(viewsets.ModelViewSet):
    serializer_class = FormChoiceSerializer
    # pagination_class = LargeResultsSetPagination
    queryset = FormChoice.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(FormChoiceView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = FormChoice.objects.all().filter(question_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FormChoiceSerializer(queryset, many=True)
        return Response(serializer.data)


class FormResponseView(viewsets.ModelViewSet):
    serializer_class = FormResponseSeializer
    # pagination_class = LargeResultsSetPagination
    queryset = FormResponse.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
            # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        if self.request.method == 'DELETE':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(FormResponseView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = FormResponse.objects.all().filter(choice_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FormResponseSeializer(queryset, many=True)
        return Response(serializer.data)


class FormRecipientView(viewsets.ModelViewSet):
    serializer_class = FormRecipientSeializer
    # pagination_class = LargeResultsSetPagination
    queryset = FormRecipient.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated,)
        return super(FormRecipientView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = FormRecipient.objects.all().filter(recipient_poll_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FormRecipientSeializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FormRecipientSeializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def form(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        # .distinct('recipient')
        queryset = FormRecipient.objects.all().filter(
            recipient_poll_id=pk).values('recipient_id').distinct()

        # newlist = []
        # for i in queryset:
        #     print(i)
        #     if i.recipient_id not in newlist:
        #         newlist.append(i.recipient_id)

        # print(newlist)

        serializer = FormRecipientSeializer(queryset, many=True)
        return Response(serializer.data)
