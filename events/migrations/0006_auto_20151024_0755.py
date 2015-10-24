# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_events_supporters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='supporters',
        ),
        migrations.AddField(
            model_name='events',
            name='supporters',
            field=models.ManyToManyField(to='events.Supporters', null=True),
        ),
    ]
