# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opiekun', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opiekun',
            name='grupy',
        ),
        migrations.AddField(
            model_name='opiekun',
            name='grupy',
            field=models.ManyToManyField(to='opiekun.Grupa'),
        ),
    ]
