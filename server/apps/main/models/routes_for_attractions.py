from functools import partial
from typing import final

from django.db import models

from server.utilites import build_upload_path
from .attraction_description import Attraction



@final
class Route(models.Model):
    attraction = models.OneToOneField(
        to=Attraction,
        on_delete=models.CASCADE,
        related_name='routes'
    )

    audio_description = models.FileField(
        upload_to=partial(build_upload_path, base_path='audio'),
        null=True,
        blank=True,
        verbose_name='Аудио описание маршрутов'
    )


    class Meta:
        db_table = 'routes'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


    def __str__(self) -> str:
        return 'route <{}>'.format(self.id)



@final
class MetroStation(models.Model):

    class StationTypeVariants(models.TextChoices):
        METRO = ('m', 'станция метро')
        MCC = ('mcc', 'станция МЦК')


    related_route = models.ForeignKey(
        to=Route,
        on_delete=models.CASCADE,
        related_name='metro_stations'
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
