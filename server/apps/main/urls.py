from django.urls import path

from .views import (
    index,
    show_about_site_info,
    show_attraction_detail,
    show_attraction_list,
    show_routes_for_attraction
)



urlpatterns = (
    path('', index, name='index'),
    path('about/', show_about_site_info, name='about'),
    path('attractions/', show_attraction_list, name='show_attraction_list'),
    path('attractions<int:attraction_id>/', show_attraction_detail, name='attraction_detail'),
    path('attractions<int:attraction_id>/routes/', show_routes_for_attraction, name='routes')
)
