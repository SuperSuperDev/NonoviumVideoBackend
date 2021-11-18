from django.contrib import admin

from nonovium_video_backend.video_encoder.admin import FormatInline

from .models import Video, VideoPost


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = (FormatInline,)

    list_display = ("title", "width", "height", "duration", "size")
    fields = (
        "title",
        "file",
        "width",
        "height",
        "duration",
        "thumbnail",
        "size",
    )
    readonly_fields = ("width", "height", "duration", "size")


# admin.site.register(VideoPost)


@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "slug",
        "post_id",
        "publish_status",
        "privacy_status",
    )
    fields = (
        "title",
        "video",
        "publish_status",
        "privacy_status",
        "post_id",
        "slug",
        "description",
        "timestamp",
        "updated",
        "short_description",
        "user",
        "pk",
    )
    readonly_fields = ("post_id", "slug", "timestamp", "updated", "user", "pk")
