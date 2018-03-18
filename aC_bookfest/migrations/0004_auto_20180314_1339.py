# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aC_bookfest', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('L', 'Lesbian'), ('G', 'Gay'), ('B', 'Bisexual'), ('T', 'Transgender'), ('Q', 'Queer')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2, null=True),
        ),
    ]