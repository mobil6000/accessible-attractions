from result import Err, Ok, Result

from server.apps.main.models import AboutUsPage
from server.utilites import catch_database_errors, ErrorReason, md_to_html



def get_about_site_info() -> Result[str, ErrorReason]:
    return _fetch_data().map(md_to_html)


@catch_database_errors
def _fetch_data() -> Result[str, ErrorReason]:
    data: str | None = AboutUsPage.objects.values_list('content', flat=True).first()
    if data is None:
        return Err(ErrorReason('data of <about us> page is not exists'))
    else:
        return Ok(data)
