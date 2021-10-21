from django.contrib.contenttypes.fields import GenericRelation
from django.db import models, transaction
from video_encoding.fields import ImageField, VideoField
from video_encoding.models import Format

# from nonovium_video_backend.users.models import User


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    uploaded_video = models.FileField(upload_to="videos/", blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    thumbnail = ImageField(null=True, blank=True)
    file = VideoField(
        width_field="width", height_field="height", duration_field="duration"
    )
    video_360 = VideoField(
        editable=False,
        null=True,
        blank=True,
        width_field="width",
        height_field="height",
        duration_field="duration",
    )
    video_sd = VideoField(
        editable=False,
        null=True,
        blank=True,
        width_field="width",
        height_field="height",
        duration_field="duration",
    )

    format_set = GenericRelation(Format)

    def save(self, *args, **kwargs):
        from .tasks import encode_video

        super(Video, self).save(*args, **kwargs)
        if self.file:
            transaction.on_commit(lambda: encode_video.delay(self.id))


class VideoPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    short_description = models.TextField(blank=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="video_posts",
        null=True,
        blank=True,
    )
    uploaded_video = models.FileField(upload_to="videos/", blank=True)
    video = models.ForeignKey(
        "videos.Video",
        on_delete=models.CASCADE,
        related_name="video_posts",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.video}"

    class Meta:
        ordering = ["-timestamp"]
