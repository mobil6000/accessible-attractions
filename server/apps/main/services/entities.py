'''
Business entities used in the service layer.
'''

from typing import final, NamedTuple



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str



@final
class AttractionDetail(NamedTuple):
    title: str
    description: str
    audio_description_url: str



@final
class Route(NamedTuple):
    title: str
    text_description: str
