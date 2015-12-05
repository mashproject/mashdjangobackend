from boto.ses import SESConnection

from rest_framework.views import APIView

from django.shortcuts import render
from mail.forms import SendMailForm
from mail.models import Mail
from mash_backend.settings.production import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DEFAULT_EMAIL_SENDER


# todo make async
class SendMail(APIView):
    def get(self, request):
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': SendMailForm()})

    def post(self, request):
        mail_form = SendMailForm(request.POST)
        connection = SESConnection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        if mail_form.is_valid():
            try:
                emails = Mail.objects.all().values_list('email', flat=True)
            except Mail.DoesNotExist:
                emails = []
            connection.send_email(DEFAULT_EMAIL_SENDER, mail_form.cleaned_data['subject'],
                                  mail_form.cleaned_data['body'], emails)
            send_errors = dict(message='Triggered Func')

        else:
            send_errors = dict(message=mail_form.errors)
        return render(request, 'send_mail_form.html',
                      {'send_mail_form': mail_form, 'send_errors': send_errors})
