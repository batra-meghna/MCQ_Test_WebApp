# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-18 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstest',
            name='completion_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userstest',
            name='test_started',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userstest',
            name='ans_array',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='userstest',
            name='que_array',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='userstest',
            name='test_progress',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
