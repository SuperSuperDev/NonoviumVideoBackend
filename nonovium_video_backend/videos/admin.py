from django.contrib import admin

from nonovium_video_backend.video_encoder.admin import FormatInline

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
        "thumbnail",
    )
    readonly_fields = ("width", "height", "duration")


admin.site.register(VideoPost)
