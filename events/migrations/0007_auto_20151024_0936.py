# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20151024_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='supporters',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
