'''
Set of service functions that manipulate data about attractions and other related information.
'''

from returns.result import Failure, Result, safe, Success

from server.apps.main.models import Attraction
from .entities import AttractionDetail, AttractionPreview
from .exceptions import DataMissingError
from .helpers import ErrorReason, is_successful_result



def get_attraction_previews() -> Result['list[AttractionPreview]', ErrorReason]:
    '''Extractes short information about all attractions'''
    result_of_selection = __fetch_attraction_preview_data()
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('error'))
    attraction_previews = [AttractionPreview(*row) for row in result_of_selection.unwrap()]
    return Success(attraction_previews)


def get_attraction_detail(attraction_id: int) -> Result['AttractionDetail', ErrorReason]:
    result_of_selection = __fetch_attraction_detail_data(attraction_id)
    if not is_successful_result(result_of_selection):
        return Failure(ErrorReason('error'))
    title, description = result_of_selection.unwrap()
    return Success(AttractionDetail(title, description))


@safe
def __fetch_attraction_preview_data() -> list[tuple[int, str, str]]:
    field_names = ('id', 'name', 'short_info',)
    query_set = Attraction.objects.values_list(*field_names)
    if not query_set.exists():
        raise DataMissingError('not a single attraction was found')
    return list(query_set.iterator())


@safe
def __fetch_attraction_detail_data(attraction_id: int) -> tuple[str, str]:
    field_names = ('name', 'description',)
    data = Attraction.objects.values_list(*field_names).get(id=attraction_id)
    return data
