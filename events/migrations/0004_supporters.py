# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151004_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(upload_to=events.models.image_path, blank=True)),
                ('type_id', models.IntegerField(default=0, choices=[(0, b'Organiser'), (1, b'Sponsors')])),
            ],
        ),
    ]
