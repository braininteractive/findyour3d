# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20170921_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='budget',
            field=models.IntegerField(choices=[(0, 'Less than $100'), (1, '$100 - 250'), (2, '$250 - 500'), (3, '$500 - 2,500'), (4, '$2,500 plus')], default=0),
        ),
    ]
