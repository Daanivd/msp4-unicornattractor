# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_auto_20190724_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='tag',
        ),
        migrations.AddField(
            model_name='feature',
            name='devComments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
