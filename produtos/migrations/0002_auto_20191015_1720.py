# Generated by Django 2.2.4 on 2019-10-15 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='detalhes_da_pagina_inicial_ingles',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='detalhes_ingles',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='nome_ingles',
        ),
    ]
