from django.urls import path
from .views_mp4 import mp4_formats, mp4_download
from .views_mp3 import mp3_formats, mp3_download

urlpatterns = [
    path("mp4/formats/", mp4_formats),
    path("mp4/download/", mp4_download),

    path("mp3/formats/", mp3_formats),
    path("mp3/download/", mp3_download),
]
