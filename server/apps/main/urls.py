from django.urls import path

from .views import index, show_attraction_detail, show_attraction_list



urlpatterns = (
    path('', index, name='index'),
    path('attractions/', show_attraction_list, name='show_attraction_list'),
    path('attractions<int:attraction_id>/', show_attraction_detail, name='attraction_detail'),
)
