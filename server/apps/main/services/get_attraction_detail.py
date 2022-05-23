from markdown import markdown
from result import Err, Ok, Result

from server.apps.main.models import Attraction, Photo
from .entities import AttractionDetail, AttractionImage
from .helpers import catch_database_errors, ErrorReason



def get_attraction_detail(attraction_id: int) -> Result[AttractionDetail, ErrorReason]:
    return _fetch_data(attraction_id).map(_construct_total_object)


@catch_database_errors
def _fetch_data(attraction_id: int) -> Result[tuple[Attraction, list[Photo]], ErrorReason]:
    try:
        attraction_data: Attraction = Attraction.objects.get(id=attraction_id)
    except Attraction.DoesNotExist as catched_exception:
        return Err(ErrorReason(str(catched_exception)))
    attraction_image_data = list(attraction_data.photos.all())
    return Ok((attraction_data, attraction_image_data))


def _construct_total_object(raw_data: tuple[Attraction, list[Photo]]) -> AttractionDetail:
    result_object = AttractionDetail(raw_data[0].name)
    result_object.description = markdown(raw_data[0].description)
    result_object.audio_description_url = raw_data[0].audio_description.url
    result_object.related_photos = [
        AttractionImage(item.caption, item.image.url)
        for item in raw_data[1]
    ]
    return result_object
