# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
