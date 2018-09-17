from django.urls import path
from .views import ListDocumentsView


urlpatterns = [
    path('articles/', ListDocumentsView.as_view(), name="articles-all")
]