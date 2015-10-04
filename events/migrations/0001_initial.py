# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('edit_date', models.DateField(auto_now=True, verbose_name=b'date edited')),
                ('pub_date', models.DateField(null=True, verbose_name=b'date published')),
                ('is_published', models.BooleanField(default=False)),
                ('type_id', models.IntegerField(default=0, choices=[(0, b'Default'), (1, b'Events')])),
                ('gallery_div', models.TextField()),
            ],
        ),
    ]
