# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-11 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aC_bookfest', '0002_auto_20180408_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='orders',
        ),
        migrations.AddField(
            model_name='event',
            name='orders',
            field=models.ManyToManyField(through='aC_bookfest.Order', to='aC_bookfest.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(db_column='studentId', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='aC_bookfest.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='event',
            field=models.ForeignKey(db_column='eventId', on_delete=django.db.models.deletion.CASCADE, to='aC_bookfest.Event'),
        ),
    ]