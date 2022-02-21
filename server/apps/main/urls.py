from django.urls import path

from . import views



urlpatterns = (
    path(route='', view=views.index, name='index'),
    path(route='attractions/', view=views.show_attractions_list, name='show_attractions_list')
)
