# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location_latitude',
            field=models.FloatField(default='-1', verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='post',
            name='location_longitude',
            field=models.FloatField(default='-1', verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
    ]