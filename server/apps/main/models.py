from typing import final

from django.db import models



@final
class Attraction(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название достопримечательности')
    description = models.TextField(verbose_name='Описание')
    route = models.TextField(verbose_name='Маршрут до объекта')
    return_route = models.TextField(verbose_name='Обратный маршрут')


    class Meta:
        db_table = 'attractions'
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


    def __str__(self) -> str:
        return 'Attraction <{0}>'.format(self.name)
