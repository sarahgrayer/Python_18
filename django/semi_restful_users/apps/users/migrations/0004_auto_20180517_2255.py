# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-18 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180517_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
