# Business logic of application
from typing import final, NamedTuple

from server.apps.main import models
from .exceptions import DataMissingError



@final
class ShortAttractionRecord(NamedTuple):
    name: str
    short_info: str


def fetch_attractions_list() -> list[ShortAttractionRecord]:
    query = models.Attraction.objects.values('name', 'short_info')
    has_data = query.exists()
    if not has_data:
        raise DataMissingError('there are no attractions!')
    return [ShortAttractionRecord(**row) for row in query.iterator()]
