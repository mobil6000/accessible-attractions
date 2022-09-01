from typing import final, NamedTuple

from server.apps.main.models import Attraction
from server.utilites import BusinessLogicFailure, handle_db_errors



@final
class AttractionPreview(NamedTuple):
    '''
    structure of a short description of the attraction
    '''

    attraction_id: int
    name: str
    short_info: str



@handle_db_errors
def get_attraction_previews() -> list[AttractionPreview]:
    '''
    Returnes short information about all attractions.
    Raises an exception <Business Logic Failure> in case of an error
    '''

    field_names = ('id', 'name', 'short_info',)
    query_set = Attraction.objects.values_list(*field_names)
    data = [AttractionPreview(*row) for row in query_set]
    if not data:
        raise BusinessLogicFailure('not a single attraction was found')
    else:
        return data
