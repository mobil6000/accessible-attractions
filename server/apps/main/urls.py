from django.urls import path

from .views import (
    index,
    show_attraction_detail,
    show_attractions_list,
    show_help,
    show_routes_for_attraction
)



urlpatterns = (
    path('', index, name='index'),
    path('about/', show_help, name='about'),
    path('attractions/', show_attractions_list, name='attractions_list'),
    path('attractions<int:attraction_id>/', show_attraction_detail, name='attraction_detail'),
    path('attractions<int:attraction_id>/routes/', show_routes_for_attraction, name='routes')
)
