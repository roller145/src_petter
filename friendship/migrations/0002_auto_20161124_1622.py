# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-24 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='date_replied',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438'),
        ),
    ]
