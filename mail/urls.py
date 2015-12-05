from django.conf.urls import url
from mail import views

__author__ = 'aman'

urlpatterns = [
   url(r'^send_mail/$', views.SendMail().as_view(), name='send_mail'),
]