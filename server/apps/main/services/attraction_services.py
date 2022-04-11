'''
Set of service functions that manipulate data about attractions and other related information.
'''

from returns.result import Failure, Result, safe, Success

from server.apps.main import models
from .entities import AttractionPreview
from .exceptions import DataMissingError
from .helpers import ErrorReason, is_successful_result



def get_attraction_previews() -> Result['list[AttractionPreview]', ErrorReason]:
    '''Extractes short information about all attractions'''
    result_of_selection = __fetch_attraction_preview_data()
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('error'))
    attraction_previews = [AttractionPreview(*row) for row in result_of_selection.unwrap()]
    return Success(attraction_previews)


@safe
def __fetch_attraction_preview_data() -> list[tuple[int, str, str]]:
    extracted_field_names = ('id', 'name', 'short_info')
    query_set = models.Attraction.objects.values_list(*extracted_field_names)
    if not query_set.exists():
        raise DataMissingError('not a single attraction was found')
    return list(query_set.iterator())
