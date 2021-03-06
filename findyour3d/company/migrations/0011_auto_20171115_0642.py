# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 06:42
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20170929_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='material',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'PLA (Polylactide)'), (1, 'ABS (Acrylonitrile Butadiene Styrene)'), (2, 'ABS-Like'), (3, 'PETG (Polyethylene Terephthalate)'), (4, 'TPE (Thermoplastic Elastomers)'), (5, 'PC (Polycarbonate)'), (6, 'Nylon'), (7, 'Reinforced Nylon'), (8, 'Sandstone'), (9, 'Stainless Steel'), (10, 'Titanium'), (11, 'Aluminum'), (12, 'Silver / Gold'), (13, 'Copper'), (14, 'Inconel'), (15, 'Wood-Like'), (16, 'PEEK'), (17, 'PEI'), (18, 'Alumide'), (19, 'Resins')], max_length=49, null=True),
        ),
    ]
