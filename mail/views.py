from rest_framework.views import APIView

from django.core.mail import send_mail
from django.shortcuts import render
from mail.forms import SendMailForm


class SendMail(APIView):
    def get(self, request):
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': SendMailForm()})

    def post(self, request):
        send_mail('Subject here', 'Here is the message.', 'ads71993@gmail.com',
                  ['ads71993@gmail.com'], fail_silently=False)
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': SendMailForm()})
