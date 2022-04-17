from django.conf import settings
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('server.apps.main.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # noqa: WPS433
    urlpatterns += static(  # type: ignore
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
