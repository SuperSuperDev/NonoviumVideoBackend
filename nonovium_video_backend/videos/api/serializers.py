from rest_framework import serializers

from nonovium_video_backend.video_encoder.api.serializers import FormatSerializer
from nonovium_video_backend.videos.models import Video, VideoPost


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # fields = ('id', 'title', 'width', 'height', 'duration', 'thumbnail', 'file')
        fields = "__all__"


class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        # fields = ('id', 'title', 'description', 'short_description', 'video', 'user')
        fields = "__all__"


class PopulatedVideoSerializer(VideoSerializer):
    format_set = FormatSerializer(many=True)


class PopulatedVideoPostSerializer(VideoPostSerializer):
    video = PopulatedVideoSerializer()
