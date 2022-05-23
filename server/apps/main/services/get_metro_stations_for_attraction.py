from result import Err, Ok, Result

from server.apps.main.models import MetroStation
from .entities import Route
from .helpers import catch_database_errors, ErrorReason



def get_metro_stations_for_attraction(
    attraction_id: int
) -> Result[tuple[list[str], list[Route]], ErrorReason]:
    return _fetch_data(attraction_id).map(_build_total_result)


@catch_database_errors
def _fetch_data(related_attraction_id: int) -> Result[list[dict[str, str]], ErrorReason]:
    field_names = ('station_name', 'station_type', 'route_from_station', 'route_to_station')
    query_set = MetroStation.objects.filter(
        attraction_id=related_attraction_id
    ).values(*field_names)
    data = list(query_set)
    if not data:
        return Err(ErrorReason('not a single metro station was found'))
    else:
        return Ok(data)


def _build_total_result(raw_data: list[dict[str, str]]) -> tuple[list[str], list[Route]]:
    metro_station_names = _generate_metro_station_names(raw_data)
    routes = _generate_routes(raw_data)
    return metro_station_names, routes


def _generate_metro_station_names(raw_data: list[dict[str, str]]) -> list[str]:
    names = []
    for entry in raw_data:
        if entry['station_type'] == 'm':
            station_name = 'станция метро "{}"'.format(entry['station_name'])
        else:
            station_name = 'станция МЦК "{}"'.format(entry['station_name'])
        names.append(station_name)
    return names


def _generate_routes(raw_data: list[dict[str, str]]) -> list[Route]:
    template1 = 'маршрут от станции {} до объекта'
    template2 = 'маршрут от объекта до станции {}'
    routes = []
    for entry in raw_data:
        routes.append(Route(template1.format(entry['station_name']), entry['route_from_station']))
        routes.append(Route(template2.format(entry['station_name']), entry['route_to_station']))
    return routes
