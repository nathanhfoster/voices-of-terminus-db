from django.urls import path
from .views import DocumentsView

urlpatterns = [
    path('articles/', DocumentsView.as_view(), name="articles"),
   ]