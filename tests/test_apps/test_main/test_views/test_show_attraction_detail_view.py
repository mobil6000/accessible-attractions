from collections import namedtuple
from typing import Final

from django.test import Client

from server.apps.main import views
from server.utilites import BusinessLogicFailure


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


def mok_business_service(fake_argument: int) -> _FakeResultDataStructure:
    images = (
        _Fake_Image_description('good photo', 'photo1.jpg'),
        _Fake_Image_description('enother photo', 'photo2.jpg'),
    )
    return _FakeResultDataStructure('some place', 'good article', 'rec.mp3', images)


def mok_business_service_with_error() -> None:
    '''
    Fake failed business scenario
    '''

    raise BusinessLogicFailure


def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that url for getting
    detailes for concrete attraction returns correct status
    '''

    monkeypatch.setattr(views, 'get_attraction_detail', mok_business_service)
    response = client.get('/attractions7/')
    assert response.status_code == 200


def test_response_content(client: Client, monkeypatch) -> None:
    '''
    This test ensures that url for getting
    detailes for concrete attraction returns correct data
    '''

    monkeypatch.setattr(views, 'get_attraction_detail', mok_business_service)
    response = client.get('/attractions3/')
    page_content = response.content.decode()
    expected_result = mok_business_service(fake_argument=6)
    assert page_content.find(expected_result.title) > 0
    assert page_content.find(expected_result.description) > 0


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
