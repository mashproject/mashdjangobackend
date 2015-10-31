# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gallery_div',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='regiteration_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
