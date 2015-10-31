# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fb_profile',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin_profile',
            field=models.URLField(blank=True),
        ),
    ]
