# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-07 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20190807_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='province',
        ),
    ]
