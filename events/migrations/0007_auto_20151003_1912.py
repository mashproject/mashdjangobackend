# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20151003_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type_id',
            field=models.IntegerField(default=0),
        ),
    ]
