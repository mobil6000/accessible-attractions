from functools import partial
from typing import final

from django.db import models

from server.utilites import build_upload_path



@final
class Attraction(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    short_info = models.CharField(max_length=256, unique=True, verbose_name='краткое описание')
    description = models.TextField(verbose_name='Описание')
    audio_description = models.FileField(
        upload_to=partial(build_upload_path, base_path='audio'),
        null=True,
        blank=True,
        verbose_name='Аудио описание'
    )
    routes_audio = models.FileField(
        upload_to=partial(build_upload_path, base_path='audio'),
        null=True,
        blank=True,
        verbose_name='Аудио описание маршрутов'
    )


    class Meta:
        db_table = 'attractions'
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


    def __str__(self) -> str:
        return 'Attraction <{}>'.format(self.name)



@final
class Photo(models.Model):
    attraction = models.ForeignKey(
        to=Attraction,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    caption = models.CharField(max_length=128, unique=True, verbose_name='Подпись')
    image = models.ImageField(
        upload_to=partial(build_upload_path, base_path='photo'),
        verbose_name='Изображение'
    )


    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


    def __str__(self) -> str:
        return 'photo <{}>'.format(self.caption)
