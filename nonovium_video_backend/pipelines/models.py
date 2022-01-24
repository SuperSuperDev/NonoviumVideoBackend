# from os.path import splitext
import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models, transaction

from nonovium_video_backend.pipelines.utils import get_local_path
from nonovium_video_backend.video_encoder.backends import get_backend
from nonovium_video_backend.video_encoder.models import Format


def short_video_id():
    return uuid.uuid4().hex[:12]


def user_directory_path(instance, filename):
    return "{0}/{1}".format(instance.video_id, filename)


class VideoFile(models.Model):
    # def _get_width(self):
    #     """
    #     Returns video width in pixels.
    #     """
    #     return self._get_video_info().get("width", 0)

    # width = property(_get_width)

    # def _get_size(self):
    #     """
    #     Returns the size of the video file, in bytes.
    #     """
    #     return self._get_video_info().get("size", 0)

    # size = property(_get_size)

    # def _get_height(self):
    #     """
    #     Returns video height in pixels.
    #     """
    #     return self._get_video_info().get("height", 0)

    # height = property(_get_height)

    # def _get_duration(self):
    #     """
    #     Returns duration in seconds.
    #     """
    #     return self._get_video_info().get("duration", 0)

    # duration = property(_get_duration)

    # def _get_video_info(self):
    #     """
    #     Returns basic information about the video as dictionary.
    #     """
    #     if not hasattr(self, "_info_cache"):
    #         encoder_backend = get_backend()

    #         with get_local_path(self) as local_path:
    #             info_cache = encoder_backend.get_media_info(local_path)

    #         self._info_cache = info_cache

    #     return self._info_cache

    file = models.FileField(upload_to=user_directory_path)
    video_id = models.CharField(primary_key=False, max_length=12, default=short_video_id, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    size = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="video_files",
        null=True,
        blank=True,
    )
    format_set = GenericRelation(Format)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        """
        Save and convert the video to the all formats.
        """
        from .tasks import convert_video_file_task

        super(VideoFile, self).save(*args, **kwargs)
        if self.file:
            transaction.on_commit(
                lambda: convert_video_file_task.delay(
                    self._meta.app_label, self._meta.model_name, self.pk
                )
            )

    print(user_directory_path)
