from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.DocumentView)
router.register('comments', views.CommentView)

urlpatterns = [
    path('', include(router.urls))
]