from typing import final, NamedTuple

from result import Err, Ok, Result

from server.apps.main.models import Attraction
from .helpers import catch_database_errors, ErrorReason



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str


def get_attraction_previews() -> Result[list[AttractionPreview], ErrorReason]:
    '''
    Extractes short information about all attractions
    '''
    return _fetch_data().map(_build_preview_objects)


@catch_database_errors
def _fetch_data() -> Result[list[tuple[int, str, str]], ErrorReason]:
    field_names = ('id', 'name', 'short_info',)
    query_set = Attraction.objects.values_list(*field_names)
    data = list(query_set)
    if not data:
        return Err(ErrorReason('not a single attraction was found'))
    else:
        return Ok(data)


def _build_preview_objects(raw_data) -> list[AttractionPreview]:
    return [AttractionPreview(*row) for row in raw_data]
