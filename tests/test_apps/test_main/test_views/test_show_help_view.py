import re
from typing import Final

from django.test import Client

from server.apps.main import views
from server.utilites import BusinessLogicFailure



FAKE_DATA: Final = 'some useful text'
PAGE_TITLE: Final = r' *<title>О нас</title>'
FAKE_ARTICLE: Final = r' *<article.*>some useful text</article>'


def mok_business_service_with_error() -> None:
    '''
    Fake failed business scenario
    '''

    raise BusinessLogicFailure


def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that the url of the help page returns the correct status
    '''

    monkeypatch.setattr(views, 'get_about_site_info', lambda: FAKE_DATA)
    response = client.get('/about/')
    assert response.status_code == 200


def test_response_content(client: Client, monkeypatch) -> None:
    '''
    This test ensures that the url of the help page returns the correct content
    '''

    monkeypatch.setattr(views, 'get_about_site_info', lambda: FAKE_DATA)
    response = client.get('/about/')
    page_content = response.content.decode()
    assert re.search(PAGE_TITLE, page_content)
    assert re.search(FAKE_ARTICLE, page_content)


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying help handles errors correctly
    '''

    monkeypatch.setattr(views, 'get_about_site_info', mok_business_service_with_error)
    response = client.get('/about/')
    assert response.status_code == 404
