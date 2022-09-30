from typing import Final

from django.test import Client

from server.apps.main import views
from tests.utilites.moks import mok_business_service_with_error



FAKE_DATA: Final = 'some useful magic text'
PAGE_TEMPLATE_NAME: Final = 'main/about_us.html'


def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that the url of the help page returns the correct status
    '''

    monkeypatch.setattr(views, 'get_about_site_info', lambda: FAKE_DATA)
    response = client.get('/about/')
    assert response.status_code == 200


def test_template_name(client: Client, monkeypatch) -> None:
    '''
    This test ensures that the view function of the help page returns the correct content
    '''

    monkeypatch.setattr(views, 'get_about_site_info', lambda: FAKE_DATA)
    response = client.get('/about/')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying help handles errors correctly
    '''

    monkeypatch.setattr(views, 'get_about_site_info', mok_business_service_with_error)
    response = client.get('/about/')
    assert response.status_code == 404
