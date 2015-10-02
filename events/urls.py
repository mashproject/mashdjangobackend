from events.views import RetrieveAll

__author__ = 'aman'

from django.conf.urls import url

urlpatterns = [
    url(r'^$', RetrieveAll.as_view())
]
