# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aC_bookfest', '0010_auto_20180322_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_checkin',
            field=models.DateTimeField(null=True),
        ),
    ]
