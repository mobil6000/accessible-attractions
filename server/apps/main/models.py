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
        upload_to=partial(build_upload_path, 'audio'),
        null=True,
        blank=True,
        verbose_name='Аудио описание'
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
        upload_to=partial(build_upload_path, 'photo'),
        verbose_name='Изображение'
    )


    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


    def __str__(self) -> str:
        return 'photo <{}>'.format(self.caption)



@final
class MetroStation(models.Model):

    class StationTypeVariants(models.TextChoices):
        METRO = ('m', 'станция метро')
        MCC = ('mcc', 'станция МЦК')

    attraction = models.ForeignKey(
        to=Attraction,
        on_delete=models.CASCADE,
        related_name='nearest_metro_stations'
    )
    station_name = models.CharField(max_length=80, unique=True, verbose_name='Название станции')
    station_type = models.CharField(
        max_length=3,
        choices=StationTypeVariants.choices,
        default=StationTypeVariants.METRO,
        verbose_name='Тип станции'
    )
    route_from_station = models.TextField(verbose_name='Маршрут от станции до объекта')
    route_to_station = models.TextField(verbose_name='Маршрут от объекта до станции')


    class Meta:
        db_table = 'metro_stations'
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


    def __str__(self) -> str:
        return 'MetroStation:<{}>'.format(self.station_name)



@final
class AboutUsPage(models.Model):
    content = models.TextField(verbose_name='Текст')


    class Meta:
        db_table = 'about_us_page'
        verbose_name = 'О нас'


    def __str__(self) -> str:
        return '<about> page'
