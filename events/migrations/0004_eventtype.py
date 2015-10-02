# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151002_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('name', models.CharField(unique=True, max_length=100)),
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
            ],
        ),
    ]
