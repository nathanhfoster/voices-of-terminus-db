from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('galleries', views.GalleryView)
router.register('gallery/images', views.GalleryImagesView)

urlpatterns = [
    path('', include(router.urls))
]