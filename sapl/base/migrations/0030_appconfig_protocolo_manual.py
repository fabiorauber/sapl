# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-15 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_appconfig_relatorios_atos'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='protocolo_manual',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Protocolar proposição somente com recibo?'),
        ),
    ]