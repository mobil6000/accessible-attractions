from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def get_attractions_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/attractions.html', {})
