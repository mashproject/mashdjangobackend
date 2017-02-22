import time

from boto.ses import SESConnection
from mail.models import Mail
from mash_backend.settings.base import MAX_MAILS_PER_SEC
from mash_backend.settings.production import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def send_mail_data(*args,**kwargs):
    connection = SESConnection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    try:
        emails = Mail.objects.all().values_list('email', flat=True)
    except Mail.DoesNotExist:
        emails = []
    for i in range(0, len(emails), MAX_MAILS_PER_SEC):
        to_addresses = emails[i:(i + MAX_MAILS_PER_SEC)]
        connection.send_email(source=kwargs.get('sender'), subject=kwargs.get('subject'), body=kwargs.get('body'),
                              to_addresses=kwargs.get('sender'),
                              bcc_addresses=to_addresses,
                              format=format)
        time.sleep(1)
