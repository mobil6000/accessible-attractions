# Business logic of application
from typing import final, NamedTuple

from server.apps.main import models



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str



@final
class GetAttractionList:
    '''Self contained service object for extracting short information about all attractions. '''

    def __call__(self) -> list[AttractionPreview]:
        raw_data = self._fetch_data()
        result = [AttractionPreview(*row) for row in raw_data]
        return result


    def _fetch_data(self) -> list[tuple[int, str, str]]:
        extracted_field_names = ('id', 'name', 'short_info')
        query = models.Attraction.objects.values_list(*extracted_field_names)
        return list(query.iterator())
