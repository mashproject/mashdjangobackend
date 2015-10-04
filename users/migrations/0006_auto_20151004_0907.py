# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151004_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.IntegerField(null=True, choices=[(0, b'Technical'), (1, b'Communication'), (2, b'Events'), (3, b'Human Resourse'), (4, b'Finance'), (5, b'Advisors'), (6, b'Admin')]),
        ),
    ]
