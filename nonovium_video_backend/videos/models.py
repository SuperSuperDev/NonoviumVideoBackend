from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="videos/")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.file} "

    class Meta:
        ordering = ["-timestamp"]
