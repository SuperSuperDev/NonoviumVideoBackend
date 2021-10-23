from django.urls import path

from nonovium_video_backend.videos.views import video_form_view

app_name = "videos"

urlpatterns = [
    path("video_form.html", video_form_view, name="video_form"),
]
