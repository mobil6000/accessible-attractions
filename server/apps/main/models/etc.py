from typing import final

from django.db import models



@final
class AboutUsPage(models.Model):
    content = models.TextField(verbose_name='Текст')


    class Meta:
        db_table = 'about_us_page'
        verbose_name = 'О нас'


    def __str__(self) -> str:
        return '<about> page'
