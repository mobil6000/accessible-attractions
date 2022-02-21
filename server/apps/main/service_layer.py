# Business logic of application
from typing import final, NamedTuple

from . import models



@final
class DataMissingError(Exception):
    '''Exception raising in the absence of the requested data'''

    def __init__(self, error_message: str):
        self.message = error_message
        super().__init__(self, error_message)


    def __str__(self) -> str:
        return 'DataMissingError: {0}'.format(self.message)



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
