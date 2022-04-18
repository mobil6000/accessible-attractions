'''
Business entities used in the service layer.
'''

from dataclasses import dataclass
from typing import final, NamedTuple



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str



@final
class AttractionImage(NamedTuple):
    caption: str
    image_url: str



@final
@dataclass
class AttractionDetail:
    title: str
    description: str | None = None
    audio_description_url: str | None = None
    related_photos: list[AttractionImage] | None = None



@final
class Route(NamedTuple):
    title: str
    text_description: str
