from django.db.models import F
from rest_framework import permissions, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from galleries.permissions import IsOwnerOrReadOnly, IsUpdateProfile

from .models import Gallery, GalleryImages
from .serializers import GallerySerializer, GalleryImagesSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class GalleryView(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    pagination_class = StandardResultsSetPagination
    queryset = Gallery.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(GalleryView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        Gallery.objects.filter(pk=pk).update(views=F('views') + 1)
        qs = Gallery.objects.get(pk=pk)
        # Increment the view count
        # qs.views += 1
        # qs.save() # save
        return Response(GallerySerializer(qs).data)


class GalleryImagesView(viewsets.ModelViewSet):
    serializer_class = GalleryImagesSerializer
    pagination_class = StandardResultsSetPagination
    queryset = GalleryImages.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (
                permissions.IsAuthenticated, IsUpdateProfile,)
        return super(GalleryImagesView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        GalleryImages.objects.all().filter(gallery_id=pk).update(views=F('views') + 1)
        queryset = GalleryImages.objects.all().filter(gallery_id=pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GalleryImagesSerializer(queryset, many=True)
        return Response(serializer.data)
