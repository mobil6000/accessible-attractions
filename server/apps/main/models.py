from typing import final

from django.db import models



@final
class Attraction(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    short_info = models.CharField(max_length=256, unique=True, verbose_name='краткое описание')
    description = models.TextField(verbose_name='Описание')


    class Meta:
        db_table = 'attractions'
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


    def __str__(self) -> str:
        return 'Attraction <{0}>'.format(self.name)



@final
class MetroStation(models.Model):
    attraction = models.ForeignKey(
        to=Attraction,
        on_delete=models.CASCADE,
        related_name='nearest_metro_stations'
    )
    station_name = models.CharField(max_length=80, unique=True, verbose_name='Название станции')
    route_from_station = models.TextField(verbose_name='Маршрут от станции до объекта')
    route_to_station = models.TextField(verbose_name='Маршрут от объекта до станции')


    class Meta:
        db_table = 'metro_stations'
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


    def __str__(self) -> str:
        return 'MetroStation:<{0}>'.format(self.station_name)
