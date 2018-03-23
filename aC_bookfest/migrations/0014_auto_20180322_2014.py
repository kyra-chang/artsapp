# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-23 03:14
from __future__ import unicode_literals

import aC_bookfest.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aC_bookfest', '0013_event_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='aC_bookfest.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Picture',
            field=models.FileField(default='settings.MEDIA_ROOT/default.jpg', null=True, upload_to=aC_bookfest.models.event_pic_path),
        ),
    ]
