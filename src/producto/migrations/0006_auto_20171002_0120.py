# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 01:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_producto_preciocosto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precioVenta',
            new_name='precioProducto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precioCosto',
        ),
    ]
