# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-14 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0029_auto_20181024_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumoordenacao',
            name='decimo_primeiro',
            field=models.CharField(default='', max_length=30),
        ),
    ]
