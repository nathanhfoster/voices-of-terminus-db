from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tickets', views.TicketView)
router.register('ticket/notes', views.NoteView)
router.register('ticket/statusChange', views.StatusChangeView)

urlpatterns = [
    path('', include(router.urls))
]
