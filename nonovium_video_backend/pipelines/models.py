# from os.path import splitext
import uuid

from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    return "user_{0}/{1}/{2}".format(instance.user.id, instance.video_id, filename)


class VideoFile(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    size = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="video_files",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.video_id)

    print(user_directory_path)
