# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopit', '0007_make_reviews_non_translatable'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Phone number'),
        ),
    ]
