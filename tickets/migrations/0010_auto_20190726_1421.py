# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20190726_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='fix_version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='devComments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
