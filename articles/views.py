from django.db.models import F
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from articles.permissions import IsOwnerOrReadOnly, IsUpdateProfile

from .models import Article, ArticleLikes, ArticleComment
from .serializers import ArticleSerializer, ArticleLikesSerializer, ArticleCommentSerializer


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
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

class ArticleLikesView(viewsets.ModelViewSet):
    serializer_class = ArticleLikesSerializer
    queryset = ArticleLikes.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(ArticleLikesView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        qs = ArticleLikes.objects.all().filter(document_id=pk)
        serializer = ArticleLikesSerializer(qs, many=True)
        return Response(serializer.data)

class ArticleCommentView(viewsets.ModelViewSet):
    serializer_class = ArticleCommentSerializer
    queryset = ArticleComment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(ArticleCommentView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        qs = ArticleComment.objects.all().filter(document_id=pk)
        serializer = ArticleCommentSerializer(qs, many=True)
        return Response(serializer.data)