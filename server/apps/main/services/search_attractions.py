from typing import final, NamedTuple

from server.apps.main.models import Attraction
from server.utilites import handle_db_errors



@final
class AttractionHeader(NamedTuple):
    '''
    Value object representing attraction search result
    '''

    attraction_id: int
    name: str



@handle_db_errors
def search_attractions(search_query: str) -> list[AttractionHeader]:
    regexpr = rf'.*{search_query}.*'
    query_set = Attraction.objects.values_list(
        'id', 'name',
    ).filter(name__iregex=regexpr).order_by('name')
    return [AttractionHeader(*row) for row in query_set]
