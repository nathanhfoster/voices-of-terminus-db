from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('newsletters', views.NewsletterView)
router.register('newsletter/comments', views.NewsletterCommentView)

urlpatterns = [
    path('', include(router.urls))
]