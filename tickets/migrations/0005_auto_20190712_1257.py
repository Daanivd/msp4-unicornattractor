# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20190712_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='title',
            new_name='ticketName',
        ),
    ]
