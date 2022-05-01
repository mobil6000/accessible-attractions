from django.contrib import admin

from .models import Attraction, MetroStation, Photo



class PhotoInline(admin.StackedInline[Photo]):
    model = Photo
    extra = 1


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``Attraction`` model.'''
    inlines = (PhotoInline,)


@admin.register(MetroStation)
class MetroStationAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``MetroStation`` model.'''
    pass
