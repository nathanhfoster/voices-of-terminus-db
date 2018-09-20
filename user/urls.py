from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetails

urlpatterns = [
    url(r'^user/$', UserList.as_view(), name="user-list"),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetails.as_view(), name="user-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)