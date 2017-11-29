# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20171124_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cost',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='gold',
            field=models.IntegerField(blank=True),
        ),
    ]
