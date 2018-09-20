from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AccountList, AccountDetails

urlpatterns = [
    url(r'^accounts/$', AccountList.as_view(), name="account-list"),
    url(r'^accounts/(?P<pk>[0-9]+)/$', AccountDetails.as_view(), name="account-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)