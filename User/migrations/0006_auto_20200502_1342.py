# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-05-02 13:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20200502_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstest',
            name='completion_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 16, 42, 30, 802775)),
        ),
    ]
