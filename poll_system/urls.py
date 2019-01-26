from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('polls', views.PollView)
router.register('poll/questions', views.PollQuestionView)
router.register('poll/choices', views.PollChoiceView)
router.register('poll/responses', views.PollResponseView)
router.register('poll/recipients', views.PollRecipientView)

urlpatterns = [
    path('', include(router.urls))
]
