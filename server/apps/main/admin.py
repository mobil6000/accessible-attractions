from django.contrib import admin

from server.apps.main.models import Attraction, MetroStation


class MetroStationInline(admin.TabularInline):
    model = MetroStation


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``Attraction`` model.'''
    inlines = (MetroStationInline,)


@admin.register(MetroStation)
class MetroStationAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``MetroStation`` model.'''
    pass
