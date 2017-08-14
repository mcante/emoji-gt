# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20170727_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha',
            new_name='fecha_entrega',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]