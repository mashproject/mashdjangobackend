from django.db import models


class Mail(models.Model):
    email = models.EmailField()


class Setting(models.Model):
    key = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
