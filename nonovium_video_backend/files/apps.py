from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilesConfig(AppConfig):
    name = "nonovium_video_backend.files"
    verbose_name = _("Files")
