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
        "video_360",
        "video_sd",
        "width",
        "height",
        "duration",
        "uploaded_video",
        "thumbnail",
    )
    readonly_fields = ("width", "height", "duration", "video_360", "video_sd")


admin.site.register(VideoPost)
