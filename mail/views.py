from rest_framework.views import APIView

from django.shortcuts import render
from mail.forms import SendMailForm
from mail.tasks import send_mail_data


# todo make async
class SendMail(APIView):
    def get(self, request):
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': SendMailForm()})

    def post(self, request):
        mail_form = SendMailForm(request.POST)
        if mail_form.is_valid():
            send_mail_data(**mail_form.cleaned_data)
            send_errors = dict(message='Triggered Maling')
        else:
            send_errors = dict(message=mail_form.errors)
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': mail_form, 'send_errors': send_errors})
