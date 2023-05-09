from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('common.urls', namespace='common')),
)

admin.site.site_header = 'Andijon Shahar'             # default: "Django Administration"
admin.site.index_title = 'Andijon Shahar hokimligi'                          # default: "Site administration"
admin.site.site_title = 'Andijon Shahar hokimligi admin paneli' # default: "Django site admin"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

