from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from returns.pipeline import is_successful

from .services.attraction_services import GetAttractionList



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    service_object = GetAttractionList()
    result = service_object()
    if not is_successful(result):
        raise Http404('error!')
    return render(request, 'main/attractions.html', {'attraction_list': result.unwrap()})
