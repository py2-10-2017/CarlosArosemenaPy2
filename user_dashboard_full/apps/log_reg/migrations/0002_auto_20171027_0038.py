# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='description',
            field=models.TextField(),
        ),
    ]
