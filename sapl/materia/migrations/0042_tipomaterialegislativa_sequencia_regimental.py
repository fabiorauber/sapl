# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0041_proposicao_numero_materia_futuro'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomaterialegislativa',
            name='sequencia_regimental',
            field=models.PositiveIntegerField(
                default=0, help_text='A sequência regimental diz respeito ao que define o regimento da Casa Legislativa sobre qual a ordem de entrada das proposições nas Sessões Plenárias.', verbose_name='Sequência Regimental'),
        ),
    ]
