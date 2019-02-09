from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('calendar/events', views.EventView)
router.register('calendar/event/groups', views.EventGroupView)
router.register('calendar/event/group/members', views.EventGroupMemberView)

urlpatterns = [
    path('', include(router.urls))
]
