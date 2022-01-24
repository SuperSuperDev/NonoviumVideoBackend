from rest_framework import serializers

from nonovium_video_backend.pipelines.models import VideoFile


# from nonovium_video_backend.video_encoder.api.serializers import FormatSerializer
class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        # fields = (
        #     'id',
        #     'title',
        #     'width',
        #     'height',
        #     'duration',
        #     'thumbnail',
        #     'file'
        #     )
        fields = "__all__"
        ReadOnlyFields = ("id", "width", "height", "duration", "size")


class VideoFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = "__all__"
        # fields = (
        #     'file',
        #     'title',
        # )


# class PopulatedVideoFileSerializer(VideoFileSerializer):
# format_set = FormatSerializer(many=True)
