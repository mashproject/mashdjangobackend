from django.db import models

class Mail(models.Model):
    email = models.EmailField()
