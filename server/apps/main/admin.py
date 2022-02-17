from django.contrib import admin

from server.apps.main.models import Attraction



@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin[Attraction]):
    '''Admin panel object for ``Attraction`` model.'''
    pass
