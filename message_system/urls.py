from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user/groups', views.UserGroupView)
router.register('messages', views.MessageView)
router.register('message/recipients', views.MessageRecipientView)

urlpatterns = [
    path('', include(router.urls))
]
