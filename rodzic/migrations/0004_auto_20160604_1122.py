# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rodzic', '0003_auto_20160604_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rodzic',
            name='dziecko',
        ),
        migrations.AddField(
            model_name='rodzic',
            name='dziecko',
            field=models.ManyToManyField(to='rodzic.Dziecko'),
        ),
        migrations.RemoveField(
            model_name='rodzic',
            name='user',
        ),
        migrations.AddField(
            model_name='rodzic',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
