import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models, transaction

from nonovium_video_backend.video_encoder.models import Format


def short_video_id():
    return uuid.uuid4().hex[:12]


def user_directory_path(instance, filename):
    return "{0}/{1}".format(instance.video_id, filename)


class VideoFile(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    video_id = models.CharField(
        primary_key=False, max_length=12, default=short_video_id, editable=False
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    size = models.PositiveIntegerField(editable=False, null=True, blank=True)
    duration = models.FloatField(editable=False, null=True)
    media_info = models.TextField(null=True, blank=True, editable=False)
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
