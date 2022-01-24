from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from nonovium_video_backend.users.api.views import UserViewSet
from nonovium_video_backend.videos.api.views import (
    VideoPostViewSet,
    # VideoUploadViewSet,
    VideoViewSet,
)
from nonovium_video_backend.pipelines.api.views import (
    VideoFileUploadViewSet,
)
# from nonovium_video_backend.videos.api.serializers import VideoPostSerializer

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r"videos", VideoViewSet, basename="video")
router.register(r"videoposts", VideoPostViewSet, basename="videopost")
router.register(r"videoUpload", VideoFileUploadViewSet, basename="videofileupload")

app_name = "api"
urlpatterns = router.urls
