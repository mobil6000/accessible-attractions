from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services import service_layer
from .services.exceptions import DataMissingError



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    try:
        attractions = service_layer.fetch_attractions_list()
    except DataMissingError:
        return HttpResponse(status=500)
    return render(request, 'main/attractions.html', {'attraction_list': attractions})
