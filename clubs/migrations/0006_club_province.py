# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20170315_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='province',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
