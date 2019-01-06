from .models import Newsletter, NewsletterLikes, NewsletterComment
from django.db.models import F
from rest_framework import viewsets, permissions, pagination
from rest_framework.permissions import AllowAny
from .serializers import NewsletterSerializer, NewsletterNoHtmlSerializer, NewsletterHtmlSerializer, NewsletterLikesSerializer, NewsletterCommentSerializer
from newsletters.permissions import IsOwnerOrReadOnly, IsUpdateProfile
from rest_framework.decorators import action
from rest_framework.response import Response


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class NewsletterView(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Newsletter.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile)
        return super(NewsletterView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        Newsletter.objects.filter(pk=pk).update(views=F('views') + 1)
        qs = Newsletter.objects.get(pk=pk)
        # Increment the view count
        # qs.views += 1
        # qs.save()  # save
        return Response(NewsletterSerializer(qs).data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def all(self, request):
        queryset = Newsletter.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = NewsletterNoHtmlSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NewsletterNoHtmlSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def html(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        qs = Newsletter.objects.get(pk=pk)
        return Response(NewsletterHtmlSerializer(qs).data)


class NewsletterLikesView(viewsets.ModelViewSet):
    serializer_class = NewsletterLikesSerializer
    pagination_class = LargeResultsSetPagination
    queryset = NewsletterLikes.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(NewsletterLikesView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = NewsletterLikes.objects.all().filter(document_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NewsletterLikesSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsletterCommentView(viewsets.ModelViewSet):
    serializer_class = NewsletterCommentSerializer
    pagination_class = LargeResultsSetPagination
    queryset = NewsletterComment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(NewsletterCommentView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = NewsletterComment.objects.all().filter(document_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NewsletterCommentSerializer(queryset, many=True)
        return Response(serializer.data)
