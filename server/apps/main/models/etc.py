from functools import partial
from typing import final

from django.core.validators import FileExtensionValidator
from django.db import models

from server.utilites import build_upload_path



@final
class AboutUsPage(models.Model):
    content = models.TextField(verbose_name='Текст')


    class Meta:
        db_table = 'about_us_page'
        verbose_name = 'О нас'


    def __str__(self) -> str:
        return '<about> page'



@final
class Video(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    video_file = models.FileField(
        upload_to=partial(build_upload_path, base_path='video'),
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        verbose_name='Видео файл',
    )


    class Meta:
        db_table = 'videos'
        verbose_name = 'Видео'


    def __str__(self) -> str:
        return self.title
