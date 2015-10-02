from events.views import RetrieveByIdView, RetrieveAll

__author__ = 'aman'

from django.conf.urls import url

urlpatterns = [
    url(r'^$', RetrieveAll.as_view()),
    url(r'^id/(?P<pk>[0-9]+)/$', RetrieveByIdView.as_view()),
]
