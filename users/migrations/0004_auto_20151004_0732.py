# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151003_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me_profile',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='about_user',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkedin_profile',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='twitter_profile',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fb_profile',
            field=models.URLField(),
        ),
    ]
