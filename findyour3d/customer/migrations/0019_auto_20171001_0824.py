# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_auto_20171001_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='shipping',
            field=models.IntegerField(blank=True, choices=[(0, 'International Shipping'), (1, 'Expedited Shipping (2-3 Days)'), (2, 'Next Day Shipping')], null=True),
        ),
    ]