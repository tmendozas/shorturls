# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-22 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('short_url', models.CharField(max_length=5)),
                ('real_url', models.TextField()),
            ],
            options={
                'db_table': 'link',
            },
        ),
    ]