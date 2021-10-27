from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from nonovium_video_backend.users.api.views import UserViewSet
from nonovium_video_backend.videos.api.views import VideoPostViewSetList

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("videos", VideoPostViewSetList)


app_name = "api"
urlpatterns = router.urls
