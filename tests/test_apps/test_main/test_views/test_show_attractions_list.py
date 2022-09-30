from collections import namedtuple
from typing import Final

from django.test import Client

from server.apps.main import views
from tests.utilites.moks import mok_business_service_with_error



_FakeDataStructure = namedtuple('_FakeDataStructure', (
    'attraction_id',
    'name',
    'short_info',
))

FAKE_RESULT: Final = [
    _FakeDataStructure(1, 'postgresql', 'database management system'),
    _FakeDataStructure(2, 'python', 'some good language'),
    _FakeDataStructure(3, 'prolog', 'some strange language'),
]

PAGE_TEMPLATE_NAME: Final = 'main/attractions.html'


def test_response_status(client: Client, monkeypatch) -> None:
    monkeypatch.setattr(views, 'get_attraction_previews', lambda: FAKE_RESULT)
    response = client.get('/attractions/')
    assert response.status_code == 200


def test_template_name(client: Client, monkeypatch) -> None:
    monkeypatch.setattr(views, 'get_attraction_previews', lambda: FAKE_RESULT)
    response = client.get('/attractions/')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying list of attractions handles errors correctly
    '''

    monkeypatch.setattr(views, 'get_attraction_previews', mok_business_service_with_error)
    response = client.get('/attractions/')
    assert response.status_code == 404
