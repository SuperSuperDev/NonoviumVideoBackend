from django.contrib import admin

from .models import VideoFile

# Register your models here.


@admin.register(VideoFile)
class VideoFileAdmin(admin.ModelAdmin):
    list_display = ("user", "file")
    fields = (
        "user",
        "file",
        "title",
        "width",
        "height",
        "size",
        "duration",
        "thumbnail",
    )
    readonly_fields = ("width", "height", "size", "duration")
