from rest_framework import serializers

from nonovium_video_backend.video_encoder.models import Format


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = "__all__"
