# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(blank=True, max_length=200, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
    ]
