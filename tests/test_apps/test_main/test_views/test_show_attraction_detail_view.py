from collections import namedtuple
from typing import Final

from django.test import Client

from server.apps.main import views
from tests.utilites.moks import mok_business_service_with_error


_Fake_Image_description = namedtuple('_Fake_Image_description', (
    'caption',
    'image_url',
))

_FakeResultDataStructure = namedtuple('_FakeResultDataStructure', (
    'title',
    'description',
    'audio_description_url',
    'related_photos',
))

PAGE_TEMPLATE_NAME: Final = 'main/attraction_detail.html'


def mok_business_service(fake_argument: int) -> _FakeResultDataStructure:
    images = (
        _Fake_Image_description('good photo', 'photo1.jpg'),
        _Fake_Image_description('enother photo', 'photo2.jpg'),
    )
    return _FakeResultDataStructure('some place', 'good article', 'rec.mp3', images)


def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that url for getting
    detailes for concrete attraction returns correct status
    '''

    monkeypatch.setattr(views, 'get_attraction_detail', mok_business_service)
    response = client.get('/attractions7/')
    assert response.status_code == 200


def test_template_name(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view function for displaying
    detailes for concrete attraction renders correct page template
    '''

    monkeypatch.setattr(views, 'get_attraction_detail', mok_business_service)
    response = client.get('/attractions3/')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying attraction detailes handles errors correctly
    '''

    monkeypatch.setattr(
        views,
        'get_attraction_detail',
        lambda fake_argument: mok_business_service_with_error(),
    )
    response = client.get('/attractions3/')
    assert response.status_code == 404
