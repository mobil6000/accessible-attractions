from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import service_layer



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    context_data = {'attraction_list': service_layer.fetch_attractions_list()}
    return render(request, 'main/attractions.html', context=context_data)
