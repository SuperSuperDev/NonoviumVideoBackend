import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models, transaction
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from nonovium_video_backend.video_encoder.fields import ImageField, VideoField
from nonovium_video_backend.video_encoder.models import Format


class Video(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    size = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    thumbnail = ImageField(null=True, blank=True)
    file = VideoField(
        width_field="width",
        height_field="height",
        duration_field="duration",
        size_field="size",
    )

    format_set = GenericRelation(Format)

    def __str__(self):
        return self.title or self.file.name

    def save(self, *args, **kwargs):
        """
        Save and convert the video to the all formats.
        """
        from .tasks import convert_video_task

        super(Video, self).save(*args, **kwargs)
        if self.file:
            transaction.on_commit(
                lambda: convert_video_task.delay(
                    self._meta.app_label, self._meta.model_name, self.pk
                )
            )


class VideoPost(models.Model):
    class PublishStatus(models.TextChoices):
        DRAFT = "D", _("Draft")
        PUBLISHED = "P", _("Published")
        DELETED = "DLT", _("Deleted")

    class PrivacyStatus(models.TextChoices):
        PUBLIC = "PUB", _("Public")
        PRIVATE = "PRV", _("Private")
        WITH_LINK = "WLK", _("With Link")

    publish_status = models.CharField(
        max_length=3, choices=PublishStatus.choices, default=PublishStatus.PUBLISHED
    )
    privacy_status = models.CharField(
        max_length=3, choices=PrivacyStatus.choices, default=PrivacyStatus.PUBLIC
    )
    title = models.CharField(max_length=255)
    post_id = models.CharField(
        default=f"{str(uuid.uuid4())}", editable=False, null=False, max_length=256
    )
    slug = models.CharField(
        max_length=255, unique=True, default=slugify(title), blank=True, editable=False
    )
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
    video = models.ForeignKey(
        "videos.Video",
        on_delete=models.CASCADE,
        related_name="video_posts",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.video}"

    def save(self, *args, **kwargs):

        if not self.post_id:
            self.post_id = f"${str(uuid.uuid4())}"

        if not self.slug:
            self.slug = f"{slugify(self.title)}"
        super(VideoPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-timestamp"]
