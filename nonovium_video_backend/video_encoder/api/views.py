from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from nonovium_video_backend.video_encoder.api.serializers import FormatSerializer
from nonovium_video_backend.video_encoder.models import Format


class FormatListAllViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

    def get_queryset(self):
        return Format.objects.all()


# View for Formats related to a specific Video
class FormatVideoListViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

    def get_queryset(self):
        video_id = self.kwargs["object_id"]
        return Format.objects.filter(video_id=video_id)
