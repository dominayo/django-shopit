# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopit', '0008_add_phone_number_to_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcode',
            name='max_uses',
            field=models.PositiveIntegerField(blank=True, help_text='Number of times this code can be used, leave empty for unlimited usage.', null=True, verbose_name='Max uses'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='active',
            field=models.BooleanField(default=True, help_text='Is this discount code active.', verbose_name='Active'),
        ),
    ]