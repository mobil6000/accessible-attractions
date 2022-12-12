from django.urls import path

from .views import (
    index,
    show_attraction_detail,
    show_attractions_list,
    show_help,
    show_routes_for_attraction,
    show_search_results,
    show_videos,
)



urlpatterns = (
    path('', index, name='index'),
    path('videos/', show_videos, name='videos'),
    path('search/', show_search_results, name='search'),
    path('about/', show_help, name='about'),
    path('attractions/', show_attractions_list, name='attractions_list'),
    path('attractions<int:attraction_id>/', show_attraction_detail, name='attraction_detail'),
    path('attractions<int:attraction_id>/routes/', show_routes_for_attraction, name='routes')
)
