# Business logic of application
from typing import final, NamedTuple

from returns.pipeline import is_successful
from returns.result import Failure, Result, safe, Success

from server.apps.main import models
from .exceptions import DataMissingError



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str



@final
class GetAttractionList:
    '''
    Self contained callable service object that extractes short information about all attractions.
    '''

    # Define type aliases
    _RawData = list[tuple[int, str, str]]
    _Output = list[AttractionPreview]


    def __call__(self) -> Result['_Output', Exception]:
        selection_result = self._fetch_data()
        if not is_successful(selection_result):
            return Failure(selection_result.failure())
        attraction_previews = [AttractionPreview(*row) for row in selection_result.unwrap()]
        return Success(attraction_previews)


    @safe
    def _fetch_data(self) -> _RawData:
        extracted_field_names = ('id', 'name', 'short_info')
        query = models.Attraction.objects.values_list(*extracted_field_names)
        if not query.exists():
            raise DataMissingError('message')
        return list(query.iterator())
