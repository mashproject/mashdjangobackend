# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(upload_to=events.models.image_path, blank=True)),
                ('edit_date', models.DateField(auto_now=True, verbose_name=b'date edited')),
                ('pub_date', models.DateField(null=True, verbose_name=b'date published')),
                ('is_published', models.BooleanField(default=False)),
                ('type_id', models.IntegerField(default=0, choices=[(0, b'Open Dialogues'), (1, b'Mixers'), (2, b'Workshops'), (3, b'Open Dialogues'), (4, b'Mash ups'), (5, b'Culture')])),
                ('gallery_div', models.TextField()),
                ('location', models.CharField(max_length=50, null=True)),
                ('regiteration_link', models.URLField(null=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(upload_to=events.models.image_path, blank=True)),
                ('type_id', models.IntegerField(default=0, choices=[(0, b'Organiser'), (1, b'Sponsors')])),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='supporters',
            field=models.ManyToManyField(to='events.Supporter'),
        ),
    ]
