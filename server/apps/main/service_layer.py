# Business logic of application
from typing import final, NamedTuple

from . import models



@final
class ShortAttractionRecord(NamedTuple):
    name: str
    short_info: str


def fetch_attractions_list() -> list[ShortAttractionRecord]:
    query = models.Attraction.objects.values('name', 'short_info')
    return [ShortAttractionRecord(**row) for row in query.iterator()]
