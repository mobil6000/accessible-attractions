'''
Set of service objects that manipulate data about attractions and other related information.
'''

from typing import final

from returns.result import Failure, Result, safe, Success

from server.apps.main import models
from .entities import AttractionPreview
from .exceptions import DataMissingError
from .helpers import is_successful_result



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
        if not is_successful_result(selection_result):
            return Failure(selection_result.failure())
        attraction_previews = [AttractionPreview(*row) for row in selection_result.unwrap()]
        return Success(attraction_previews)


    @safe
    def _fetch_data(self) -> _RawData:
        extracted_field_names = ('id', 'name', 'short_info')
        query = models.Attraction.objects.values_list(*extracted_field_names)
        if not query.exists():
            raise DataMissingError('not a single attraction was found')
        return list(query.iterator())
