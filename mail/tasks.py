from boto.ses import SESConnection
from celery.task import task
from mash_backend.settings.production import DEFAULT_EMAIL_SENDER, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


@task
def send_mail_data(emails, mail_form):
    connection = SESConnection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    connection.send_email(DEFAULT_EMAIL_SENDER, mail_form.cleaned_data['subject'],
                                  mail_form.cleaned_data['body'], emails)
