# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-14 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190813_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='img/profilePic.png', null=True, upload_to='img'),
        ),
    ]