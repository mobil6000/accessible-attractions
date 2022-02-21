from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import service_layer



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    try:
        attractions = service_layer.fetch_attractions_list()
    except service_layer.DataMissingError:
        return HttpResponse(status=500)
    return render(request, 'main/attractions.html', {'attraction_list': attractions})
