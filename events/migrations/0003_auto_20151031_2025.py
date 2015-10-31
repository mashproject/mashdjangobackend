# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151031_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'date published', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='supporters',
            field=models.ManyToManyField(to='events.Supporter', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_id',
            field=models.IntegerField(default=0, choices=[(0, b'Default'), (1, b'Mixers'), (2, b'Workshops'), (3, b'Open Dialogues'), (4, b'Mash ups'), (5, b'Culture')]),
        ),
    ]
