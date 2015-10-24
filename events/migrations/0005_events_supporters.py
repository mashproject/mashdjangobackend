# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_supporters'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='supporters',
            field=models.ForeignKey(to='events.Supporters', null=True),
        ),
    ]
