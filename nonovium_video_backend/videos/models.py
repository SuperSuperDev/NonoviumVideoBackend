# from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# from video_encoding.fields import VideoField
# from video_encoding.models import Format

# from nonovium_video_backend.users.models import User

# Create your models here.


class Video(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="videos",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="videos/")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    short_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.file}"

    class Meta:
        ordering = ["-timestamp"]
