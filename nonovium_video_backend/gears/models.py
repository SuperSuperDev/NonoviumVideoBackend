import uuid

from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class GearFile(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    gear_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="gear_files",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.gear_id)
