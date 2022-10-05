from collections import namedtuple
from typing import Final

from django.test import Client

from server.apps.main import views
from tests.utilites.moks import mok_business_service_with_error



_FakeAttractionHeader = namedtuple('_FakeAttractionHeader', (
    'attraction_id',
    'name',
))

FAKE_SEARCH_RESULTS: Final = [
    _FakeAttractionHeader(3, 'magic name'),
    _FakeAttractionHeader(5, 'enother magic name'),
]

PAGE_TEMPLATE_NAME: Final = 'main/search_results.html'


def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that url for getting search results returns correct status
    '''

    monkeypatch.setattr(views, 'search_attractions', lambda fake_argument: FAKE_SEARCH_RESULTS)
    response = client.get('/search/?q=magic')
    assert response.status_code == 200


def test_template_name(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying search results
    renders correct page template
    '''

    monkeypatch.setattr(views, 'search_attractions', lambda fake_argument: FAKE_SEARCH_RESULTS)
    response = client.get('/search/?q=magic3')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying search results handles errors correctly
    '''

    monkeypatch.setattr(
        views,
        'search_attractions',
        lambda fake_argument: mok_business_service_with_error()
    )
    response = client.get('/search/?q=magic2')
    assert response.status_code == 404
