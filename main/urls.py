from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from main.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('', include('hashtags.urls')),
    path('', include('basket.urls')),
    path('', include('cbv.urls')),
    path('', include('parsing.urls')),
    path('', include('users.urls')),
    path('', include('mobile_devices.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)

if DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns