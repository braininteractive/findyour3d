# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_expedited',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='company',
            name='shipping',
            field=models.IntegerField(blank=True, choices=[(0, 'International Shipping'), (1, 'Expedited Shipping (2-3 Days)'), (2, 'Next Day Shipping')], null=True),
        ),
    ]