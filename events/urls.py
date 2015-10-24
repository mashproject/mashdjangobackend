from events.views import RetrieveAll, get_all_suppporters

__author__ = 'aman'

from django.conf.urls import url

urlpatterns = [
    url(r'^$', RetrieveAll.as_view()),
    url(r'^supporters$', get_all_suppporters)
]
