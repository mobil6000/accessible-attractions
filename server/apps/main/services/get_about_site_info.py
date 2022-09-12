from server.apps.main.models import AboutUsPage
from server.utilites import BusinessLogicFailure, handle_db_errors, md_to_html



@handle_db_errors
def get_about_site_info() -> str:
    data: str | None = AboutUsPage.objects.values_list('content', flat=True).first()
    if data is None:
        raise BusinessLogicFailure('data of <about us> page is not exists')
    else:
        return md_to_html(data)
