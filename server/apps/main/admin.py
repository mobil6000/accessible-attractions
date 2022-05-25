from django.contrib import admin
from django.http import HttpRequest

from .models import AboutUsPage, Attraction, MetroStation, Photo



class PhotoInline(admin.StackedInline[Photo]):
    model = Photo
    extra = 1



@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``Attraction`` model.'''
    exclude = ('routes_audio',)
    inlines = (PhotoInline,)



@admin.register(MetroStation)
class MetroStationAdmin(admin.ModelAdmin[MetroStation]):
    '''Admin panel object for ``MetroStation`` model.'''
    fields = (
        'Attraction.routes_audio',
        'station_name',
        'station_type',
        'route_from_station',
        'route_to_station'
    )



@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin[AboutUsPage]):
    '''Admin panel object for ``AboutUsPage`` model.'''

    def has_add_permission(self, request: HttpRequest) -> bool:
        if self.model.objects.count() > 0:
            return False
        else:
            return super().has_add_permission(request)
