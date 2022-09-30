from typing import Final

from django.test import Client



PAGE_TEMPLATE_NAME: Final = 'main/index.html'


def test_response_status(client: Client) -> None:
    '''
    This test ensures that url of the main page returns correct status
    '''

    response = client.get('/')
    assert response.status_code == 200


def test_template_name(client: Client) -> None:
    '''
    This test ensures that view function of the main page renders correct page template
    '''

    response = client.get('/')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME
