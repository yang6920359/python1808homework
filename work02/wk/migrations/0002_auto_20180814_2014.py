# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(auto_now_add=True, verbose_name='出生日期'),
        ),
    ]
