from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DocumentList, DocumentDetails

urlpatterns = [
    url(r'^articles/$', DocumentList.as_view(), name="article-list"),
    url(r'^articles/(?P<pk>[0-9]+)/$', DocumentDetails.as_view(), name="article-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)