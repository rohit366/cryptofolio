# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptofolio', '0005_auto_20171016_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangebalance',
            old_name='last_modified',
            new_name='timestamp',
        ),
    ]
