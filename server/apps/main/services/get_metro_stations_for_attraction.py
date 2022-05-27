from result import Err, Ok, Result

from server.apps.main.models import MetroStation, Route
from .entities import RouteEntry, RouteTextRecord
from .helpers import catch_database_errors, ErrorReason



_RawData = tuple[str, list[dict[str, str]]]


def get_metro_stations_for_attraction(
    attraction_id: int
) -> Result[tuple[list[str], list[Route]], ErrorReason]:
    return _fetch_data(attraction_id).map(_build_total_result)


@catch_database_errors
def _fetch_data(related_attraction_id: int) -> Result[_RawData, ErrorReason]:
    try:
        route_model: Route = Route.objects.get(attraction_id=related_attraction_id)
    except Route.DoesNotExist as catched_exception:
        return Err(ErrorReason(str(catched_exception)))

    field_names = ('station_name', 'station_type', 'route_from_station', 'route_to_station')
    query_set = route_model.metro_stations.values(*field_names).all()
    data = list(query_set)
    if not data:
        return Err(ErrorReason('not a single metro station was found'))
    else:
        return Ok((route_model.audio_description.url, data))


def _build_total_result(raw_data: _RawData) -> RouteEntry:
    route_entry = RouteEntry(
        audio_description=raw_data[0],
        nearest_metro_station_names=_generate_metro_station_names(raw_data[1]),
        route_text_records=_generate_route_text_records(raw_data[1]),
    )
    return route_entry


def _generate_metro_station_names(raw_data: list[dict[str, str]]) -> list[str]:
    names = []
    for entry in raw_data:
        if entry['station_type'] == 'm':
            station_name = 'станция метро "{}"'.format(entry['station_name'])
        else:
            station_name = 'станция МЦК "{}"'.format(entry['station_name'])
        names.append(station_name)
    return names


def _generate_route_text_records(raw_data: list[dict[str, str]]) -> list[RouteTextRecord]:
    template1 = 'маршрут от станции {} до объекта'
    template2 = 'маршрут от объекта до станции {}'
    routes = []
    for entry in raw_data:
        routes.append(RouteTextRecord(template1.format(
            entry['station_name']), entry['route_from_station']
        ))
        routes.append(RouteTextRecord(template2.format(
            entry['station_name']), entry['route_to_station']
        ))
    return routes
