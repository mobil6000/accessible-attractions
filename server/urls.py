'''
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.
'''

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import include, path
from django.views.generic import TemplateView



# Customizing the admin panel
admin.site.site_header = 'accessibleattractions.ru: Администрирование'
admin.site.site_title = 'Панель администратора'
admin.site.index_title = 'Начальная страница'
admin.site.unregister(Group)
admin.site.unregister(User)


# Views definitions for text static files:
robats_file_view = TemplateView.as_view(template_name='robots.txt', content_type='text/plain', )
humans_file_view = TemplateView.as_view(template_name='humans.txt', content_type='text/plain')


urlpatterns = [
    path('', include('server.apps.main.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt', robats_file_view),
    path('humans.txt', humans_file_view),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # noqa: WPS433
    urlpatterns += static(  # type: ignore
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
