from typing import final, NamedTuple

from server.apps.main.models import Video
from server.utilites import BusinessLogicFailure, handle_db_errors



@final
class VideoRecording(NamedTuple):
    title: str
    description: str
    video_file: str



@handle_db_errors
def get_videos() -> tuple[VideoRecording, ...]:
    data = tuple(VideoRecording(
        model.title, model.description, model.video_file.url
    ) for model in Video.objects.all())
    if not data:
        raise BusinessLogicFailure('not a single video was found')
    else:
        return data
