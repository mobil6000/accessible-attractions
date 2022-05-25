# Generated by Django 4.0.4 on 2022-05-25 21:16

import functools

from django.db import migrations, models

import server.utilites


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_aboutuspage_alter_attraction_audio_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='routes_audio',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=functools.partial(server.utilites.build_upload_path, *('audio',), **{}),
                verbose_name='Аудио описание маршрутов'
            ),
        ),
    ]
