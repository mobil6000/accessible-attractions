from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .services import get_attraction_detail, get_attraction_previews, is_successful_result



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attraction_list(request: HttpRequest) -> HttpResponse:
    result = get_attraction_previews()
    if not is_successful_result(result):
        raise Http404('error!')
    return render(request, 'main/attractions.html', {'attraction_list': result.unwrap()})


def show_attraction_detail(request: HttpRequest, attraction_id: int) -> HttpResponse:
    result = get_attraction_detail(attraction_id)
    if not is_successful_result(result):
        raise Http404('error!')
    response_context = {'attraction_id': attraction_id, 'attraction': result.unwrap()}
    return render(request, 'main/attraction_detail.html', response_context)
