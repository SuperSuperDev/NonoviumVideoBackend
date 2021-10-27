from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from nonovium_video_backend.videos.models import Video, VideoPost

from .serializers import PopulatedVideoPostSerializer, VideoSerializer


class VideoViewSetList(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    API endpoint that allows videos to be viewed or !edited.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned videos to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        return self.queryset()


class VideoPostViewSetList(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = VideoPost.objects.all()
    serializer_class = PopulatedVideoPostSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
