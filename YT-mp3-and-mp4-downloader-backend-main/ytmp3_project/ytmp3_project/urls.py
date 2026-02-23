from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('downloader.urls')),# MP3 App
    path('video/', include('videodl.urls')),# MP4 App
    path("api/", include("api.urls")),
]
