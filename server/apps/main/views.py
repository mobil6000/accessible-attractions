from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .services import get_attraction_previews, is_successful_result



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html', {})


def show_attractions_list(request: HttpRequest) -> HttpResponse:
    result = get_attraction_previews()
    if not is_successful_result(result):
        raise Http404('error!')
    return render(request, 'main/attractions.html', {'attraction_list': result.unwrap()})
