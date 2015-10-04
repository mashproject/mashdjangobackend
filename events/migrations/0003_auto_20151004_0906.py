# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151004_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type_id',
            field=models.IntegerField(default=0, choices=[(0, b'Open Dialogues'), (1, b'Mixers'), (2, b'Workshops'), (3, b'Open Dialogues'), (4, b'Mash ups'), (5, b'Culture')]),
        ),
    ]
