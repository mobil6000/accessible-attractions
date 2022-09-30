from collections import namedtuple
from typing import Final

from django.test import Client

from server.apps.main import views
from tests.utilites.moks import mok_business_service_with_error



_FakeMetroStationEntry = namedtuple('_FakeMetroStationEntry', (
    'station_name',
    'station_type',
    'route_from_station',
    'route_to_station',
))

_FakeResultDataStructure = namedtuple('_FakeResultDataStructure', (
    'audio_description',
    'address',
    'nearest_metro_stations',
))

PAGE_TEMPLATE_NAME: Final = 'main/routes.html'


def mok_business_service(fake_argument: int) -> _FakeResultDataStructure:
    metro_stations = (
        _FakeMetroStationEntry('magic_name', 'm', 'route one', 'route two'),
        _FakeMetroStationEntry('enother magic', 'mcc', 'route one', 'route two'),
        _FakeMetroStationEntry('magic again', 'm', 'route one', 'route two'),
    )
    return _FakeResultDataStructure('magic.mp3', 'magic address', metro_stations)



def test_response_status(client: Client, monkeypatch) -> None:
    '''
    This test ensures that url for getting routes for attraction
    returns correct status
    '''

    monkeypatch.setattr(views, 'get_metro_stations_for_attraction', mok_business_service)
    response = client.get('/attractions6/routes/')
    assert response.status_code == 200


def test_template_name(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view function for displaying routes for attraction
    renders correct page template
    '''

    monkeypatch.setattr(views, 'get_metro_stations_for_attraction', mok_business_service)
    response = client.get('/attractions2/routes/')
    page_template = response.templates[0]
    assert page_template.name == PAGE_TEMPLATE_NAME


def test_business_logic_error(client: Client, monkeypatch) -> None:
    '''
    This test ensures that view for displaying routes for attraction handles errors correctly
    '''

    monkeypatch.setattr(
        views,
        'get_metro_stations_for_attraction',
        lambda fake_argument: mok_business_service_with_error(),
    )
    response = client.get('/attractions9/routes/')
    assert response.status_code == 404
