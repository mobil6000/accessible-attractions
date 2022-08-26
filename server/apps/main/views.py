from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from server.utilites import BusinessLogicFailure
from .services import (
    get_about_site_info,
    get_attraction_detail,
    get_attraction_previews,
    get_metro_stations_for_attraction
)



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attraction_list(request: HttpRequest) -> HttpResponse:
    try:
        result = get_attraction_previews()
    except BusinessLogicFailure:
        raise Http404('error!')
    return render(request, 'main/attractions.html', {'attraction_list': result})


def show_attraction_detail(request: HttpRequest, attraction_id: int) -> HttpResponse:
    result = get_attraction_detail(attraction_id)
    if not result.is_ok():
        raise Http404('error!')
    response_context = {'attraction_id': attraction_id, 'attraction': result.unwrap()}
    return render(request, 'main/attraction_detail.html', response_context)


def show_routes_for_attraction(request: HttpRequest, attraction_id: int) -> HttpResponse:
    result = get_metro_stations_for_attraction(attraction_id)
    if not result.is_ok():
        raise Http404('error!')
    response_context = {'content': result.unwrap()}
    return render(request, 'main/routes.html', response_context)


def show_about_site_info(request: HttpRequest) -> HttpResponse:
    result = get_about_site_info()
    if not result.is_ok():
        raise Http404('error!')
    return render(request, 'main/about_us.html', {'text': result.unwrap()})
