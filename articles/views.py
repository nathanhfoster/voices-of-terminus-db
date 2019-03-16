from django.db.models import F
from rest_framework import permissions, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from articles.permissions import IsOwnerOrReadOnly, IsUpdateProfile

from .models import Article, ArticleLikes, ArticleComment
from .serializers import ArticleSerializer, ArticleNoHtmlSerializer, ArticleHtmlSerializer, ArticleLikesSerializer, ArticleCommentSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(ArticleView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        Article.objects.filter(pk=pk).update(views=F('views') + 1)
        qs = Article.objects.get(pk=pk)
        # Increment the view count
        # qs.views += 1
        # qs.save() # save
        return Response(ArticleSerializer(qs).data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def all(self, request):
        queryset = Article.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ArticleNoHtmlSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArticleNoHtmlSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def allhtml(self, request):
        queryset = Article.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ArticleSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def html(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        qs = Article.objects.get(pk=pk)
        return Response(ArticleHtmlSerializer(qs).data)


class ArticleLikesView(viewsets.ModelViewSet):
    serializer_class = ArticleLikesSerializer
    pagination_class = LargeResultsSetPagination
    queryset = ArticleLikes.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(ArticleLikesView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = ArticleLikes.objects.all().filter(document_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArticleLikesSerializer(queryset, many=True)
        return Response(serializer.data)


class ArticleCommentView(viewsets.ModelViewSet):
    serializer_class = ArticleCommentSerializer
    pagination_class = LargeResultsSetPagination
    queryset = ArticleComment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(ArticleCommentView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        queryset = ArticleComment.objects.all().filter(document_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArticleCommentSerializer(queryset, many=True)
        return Response(serializer.data)
