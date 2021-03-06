# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-06 09:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='applies_to',
            field=models.IntegerField(blank=True, choices=[(1, 'Starter'), (2, 'Premium - 3 month'), (3, 'Premium - 12 month')], null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='number_of_free_quotes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.PositiveIntegerField(blank=True, help_text='Discount value in percents, for e.g. 10 or 50', null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
