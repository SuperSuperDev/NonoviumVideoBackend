from django.contrib import admin
from video_encoding.admin import FormatInline

from .models import Video, VideoPost


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = (FormatInline,)

    list_display = ("title", "width", "height", "duration")
    fields = (
        "title",
        "file",
        "width",
        "height",
        "duration",
        "uploaded_video",
        "thumbnail",
    )
    readonly_fields = ("width", "height", "duration")


admin.site.register(VideoPost)
