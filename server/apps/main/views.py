from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from server.utilites import BusinessLogicFailure
from .services import (
    get_about_site_info,
    get_attraction_detail,
    get_attraction_previews,
    get_metro_stations_for_attraction,
    get_videos,
    search_attractions
)



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    try:
        result = get_attraction_previews()
    except BusinessLogicFailure:
        raise Http404('error!')
    return render(request, 'main/attractions.html', {'attraction_list': result})


def show_attraction_detail(request: HttpRequest, attraction_id: int) -> HttpResponse:
    try:
        result = get_attraction_detail(attraction_id)
    except BusinessLogicFailure:
        raise Http404('error!')
    response_context = {'attraction_id': attraction_id, 'attraction': result}
    return render(request, 'main/attraction_detail.html', response_context)


def show_routes_for_attraction(request: HttpRequest, attraction_id: int) -> HttpResponse:
    try:
        result = get_metro_stations_for_attraction(attraction_id)
    except BusinessLogicFailure:
        raise Http404('error!')
    response_context = {'content': result}
    return render(request, 'main/routes.html', response_context)


def show_search_results(request: HttpRequest) -> HttpResponse:
    search_query = request.GET.get('q')
    try:
        search_results = search_attractions(search_query)
    except BusinessLogicFailure:
        raise Http404('error!')
    return render(request, 'main/search_results.html', {'content': search_results})


def show_help(request: HttpRequest) -> HttpResponse:
    try:
        result = get_about_site_info()
    except BusinessLogicFailure:
        raise Http404('error!')
    return render(request, 'main/about_us.html', {'text': result})


def show_videos(request: HttpRequest) -> HttpResponse:
    try:
        result = get_videos()
    except BusinessLogicFailure:
        raise Http404('error!')
    return render(request, 'main/videos.html', {'videos': result})
