from typing import final

from django.db import models

from .attraction_description import Attraction



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
