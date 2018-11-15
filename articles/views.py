from .models import Document
from django.db.models import F
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializers import DocumentSerializer
from articles.permissions import IsOwnerOrReadOnly, IsUpdateProfile
from rest_framework.decorators import action
from rest_framework.response import Response

class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(DocumentView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        Document.objects.filter(pk=pk).update(views=F('views') + 1)
        qs = Document.objects.get(pk=pk)
        # Increment the view count
        # qs.views += 1
        # qs.save() # save
        return Response(DocumentSerializer(qs).data)


# class SingleArticleView(APIView):
#     serializer_class = DocumentSerializer
#     queryset = Document.objects.all()
#     # queryset = Document.objects.get(pk=6)
#     print("querry set Is not here",)
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         articles = [a.title for a in Document.objects.all()]
#         return Response(articles)
#
#     def get_permissions(self):
#         # allow an authenticated user to create via POST
#         if self.request.method == 'GET':
#             self.permission_classes = (AllowAny,)
#         if self.request.method == 'PATCH':
#             self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
#         return super(SingleArticleView, self).get_permissions()
