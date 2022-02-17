from django.urls import path

from . import views



urlpatterns = (
    path(route='', view=views.index, name='index'),
    path(route='attractions/', view=views.get_attractions_list, name='get_attractions_list')
)
