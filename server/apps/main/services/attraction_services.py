'''
Set of service functions that manipulate data about attractions and other related information.
'''

from returns.result import Failure, Result, safe, Success

from server.apps.main.models import Attraction, MetroStation
from .entities import AttractionDetail, AttractionPreview, Route
from .exceptions import DataMissingError
from .helpers import ErrorReason, is_successful_result



def get_attraction_previews() -> Result['list[AttractionPreview]', ErrorReason]:
    '''Extractes short information about all attractions'''
    result_of_selection = __fetch_attraction_preview_data()
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('error'))
    attraction_previews = [AttractionPreview(*row) for row in result_of_selection.unwrap()]
    return Success(attraction_previews)


def get_attraction_detail(attraction_id: int) -> Result['AttractionDetail', ErrorReason]:
    result_of_selection = __fetch_attraction_detail_data(attraction_id)
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('error'))
    title, description = result_of_selection.unwrap()
    return Success(AttractionDetail(title, description))


def get_metro_stations_for_attraction(
    attraction_id: int
) -> Result['tuple[list[str], list[Route]]', ErrorReason]:
    result_of_selection = __fetch_data_of_metro_stations(attraction_id)
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('Error'))
    raw_data = result_of_selection.unwrap()
    metro_station_names = __generate_metro_station_names(raw_data)
    routes = __generate_routes(raw_data)
    return Success((metro_station_names, routes))


@safe
def __fetch_attraction_preview_data() -> list[tuple[int, str, str]]:
    field_names = ('id', 'name', 'short_info',)
    query_set = Attraction.objects.values_list(*field_names)
    if not query_set.exists():
        raise DataMissingError('not a single attraction was found')
    return list(query_set.iterator())


@safe
def __fetch_attraction_detail_data(attraction_id: int) -> tuple[str, str]:
    field_names = ('name', 'description',)
    data = Attraction.objects.values_list(*field_names).get(id=attraction_id)
    return data


@safe
def __fetch_data_of_metro_stations(related_attraction_id: int) -> list[dict[str, str]]:
    field_names = ('station_name', 'station_type', 'route_from_station', 'route_to_station')
    query_set = MetroStation.objects.filter(
        attraction_id=related_attraction_id
    ).values(*field_names)
    return list(query_set)


def __generate_metro_station_names(raw_data: list[dict[str, str]]) -> list[str]:
    names = []
    for entry in raw_data:
        if entry['station_type'] == 'm':
            station_name = 'станция метро "{}"'.format(entry['station_name'])
        else:
            station_name = 'станция МЦК "{}"'.format(entry['station_name'])
        names.append(station_name)
    return names


def __generate_routes(raw_data: list[dict[str, str]]) -> list[Route]:
    template1 = 'маршрут от станции {} до объекта'
    template2 = 'маршрут от объекта до станции {}'
    routes = []
    for entry in raw_data:
        routes.append(Route(template1.format(entry['station_name']), entry['route_from_station']))
        routes.append(Route(template2.format(entry['station_name']), entry['route_to_station']))
    return routes
