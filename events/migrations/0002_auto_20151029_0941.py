# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
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
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='image_url',
            field=models.ImageField(upload_to=events.models.image_path, blank=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='type_id',
            field=models.IntegerField(default=0, choices=[(0, b'Open Dialogues'), (1, b'Mixers'), (2, b'Workshops'), (3, b'Open Dialogues'), (4, b'Mash ups'), (5, b'Culture')]),
        ),
        migrations.AddField(
            model_name='events',
            name='supporters',
            field=models.ManyToManyField(to='events.Supporters'),
        ),
    ]
