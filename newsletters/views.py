from .models import Newsletter
from django.db.models import F
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializers import NewsLetterSerializer
from newsletters.permissions import IsOwnerOrReadOnly, IsUpdateProfile
from rest_framework.decorators import action
from rest_framework.response import Response

class NewsLetterView(viewsets.ModelViewSet):
    serializer_class = NewsLetterSerializer
    queryset = Newsletter.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile)
        return super(NewsLetterView, self).get_permissions()

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def view(self, request, pk):
        # TODO Check that the object exist
        # Query database for the object with the given PK
        Newsletter.objects.filter(pk=pk).update(views=F('views') + 1)
        qs = Newsletter.objects.get(pk=pk)
        # Increment the view count
        # qs.views += 1
        # qs.save()  # save
        return Response(NewsLetterSerializer(qs).data)
