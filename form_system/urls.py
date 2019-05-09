from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('forms', views.FormView)
router.register('form/questions', views.FormQuestionView)
router.register('form/choices', views.FormChoiceView)
router.register('form/responses', views.FormResponseView)
router.register('form/recipients', views.FormRecipientView)

urlpatterns = [
    path('', include(router.urls))
]
