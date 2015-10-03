# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20151002_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type_id',
            field=models.IntegerField(default=0, choices=[(1, 'new')]),
        ),
    ]
