from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from hello_django.views import home
from upload.views import image_upload

urlpatterns = [
    path("", home, name="home"),
    path("upload/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
