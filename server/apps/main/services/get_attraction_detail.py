from dataclasses import dataclass
from typing import final, NamedTuple

from django.db.models.query import QuerySet

from server.apps.main.models import Attraction, Photo
from server.utilites import BusinessLogicFailure, handle_db_errors, md_to_html



@final
class Image(NamedTuple):
    '''
    Metadata about uploaded photo
    '''

    caption: str
    image_url: str



@final
@dataclass(slots=True)
class AttractionInfo:
    '''
    Detailed information about the attraction
    '''

    title: str | None = None
    description: str | None = None
    audio_description_url: str | None = None
    related_photos: list[Image] | None = None



@handle_db_errors
def get_attraction_detail(attraction_id: int) -> AttractionInfo:
    '''
    Returns detailed information about the attraction.
    Raises an exception <Business Logic Failure> in case of an error
    '''

    data = __fetch_attraction_data(attraction_id)
    if not data:
        raise BusinessLogicFailure
    result_object = AttractionInfo(title=data[0], audio_description_url=data[2])
    result_object.description = md_to_html(data[1])
    result_object.related_photos = __fetch_related_photos(attraction_id)
    return result_object


def __fetch_attraction_data(attraction_id: int) -> tuple[str, str, str] | None:
    '''
    Extracts data of a particular attraction
    '''

    try:
        data: Attraction = Attraction.objects.get(id=attraction_id)
    except Attraction.DoesNotExist:
        return None
    return data.name, data.description, data.audio_description.url


def __fetch_related_photos(attraction_id: int) -> list[Image]:
    '''
    Extracts metadata about photos associated with a particular attraction
    '''

    query_set: QuerySet[Photo] = Photo.objects.filter(attraction_id=attraction_id)
    return [Image(row.caption, row.image.url) for row in query_set]
