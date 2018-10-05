from .models import NewsLetter
from rest_framework import viewsets
from .serializers import NewsLetterSerializer

class NewsLetterView(viewsets.ModelViewSet):
    serializer_class = NewsLetterSerializer
    queryset = NewsLetter.objects.all()
