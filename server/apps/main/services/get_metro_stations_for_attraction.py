from dataclasses import dataclass
from typing import final, NamedTuple

from server.apps.main.models import MetroStation, Route
from server.utilites import BusinessLogicFailure, handle_db_errors



@final
class MetroStationEntry(NamedTuple):
    station_name: str
    station_type: str
    route_from_station: str
    route_to_station: str



@final
@dataclass(slots=True)
class RouteEntry:
    audio_description: str
    address: str
    nearest_metro_stations: list[MetroStationEntry] | None = None



@handle_db_errors
def get_metro_stations_for_attraction(
    related_attraction_id: int
) -> RouteEntry:
    try:
        route_model: Route = Route.objects.get(attraction_id=related_attraction_id)
    except Route.DoesNotExist:
        raise BusinessLogicFailure
    result_object = RouteEntry(
        route_model.audio_description.url,
        route_model.address
    )

    field_names = ('station_name', 'station_type', 'route_from_station', 'route_to_station')
    query_set = route_model.metro_stations.values_list(*field_names).all()
    result_object.nearest_metro_stations = [
        MetroStationEntry(*row) for row in query_set
    ]
    return result_object
