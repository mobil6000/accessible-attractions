from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services.attraction_services import GetAttractionList



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    service_object = GetAttractionList()
    attractions = service_object()
    return render(request, 'main/attractions.html', {'attraction_list': attractions})
