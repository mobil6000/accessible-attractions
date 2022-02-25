from django.contrib import admin

from server.apps.main.models import Attraction, MetroStation


class MetroStationInline(admin.StackedInline):
    model = MetroStation
    extra = 1


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``Attraction`` model.'''
    inlines = (MetroStationInline,)
