from django.contrib import admin as django_admin
from django.contrib.contenttypes import admin

from .models import Format


class FormatInline(admin.GenericTabularInline):
    model = Format
    fields = ("format", "progress", "file", "width", "height", "duration")
    readonly_fields = fields
    extra = 0
    max_num = 0

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


@django_admin.register(Format)
class FormatAdmin(django_admin.ModelAdmin):
    list_display = (
        "format",
        "progress",
        "file",
        "width",
        "height",
        "duration",
        "object_id",
    )
    fields = (
        "format",
        "progress",
        "file",
        "width",
        "height",
        "duration",
        "object_id",
        # "video",
        "field_name",
    )
    readonly_fields = list_display
    inlines = [FormatInline]


# django_admin.site.register(Format)
