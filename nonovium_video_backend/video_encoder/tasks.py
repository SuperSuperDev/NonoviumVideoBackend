import os
import tempfile

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.db.models.fields.files import FileField

from . import signals
from .backends import get_backend
from .backends.base import BaseEncoderBackend
from .config import settings
from .exceptions import VideoEncoderError
from .fields import VideoField
from .models import Format
from .utils import get_local_path


def convert_all_video_files(app_label, model_name, object_pk):
    """
    Automatically converts all videos of a given instance.
    """
    # get instance
    Model = apps.get_model(app_label=app_label, model_name=model_name)
    instance = Model.objects.get(pk=object_pk)

    # search for `VideoFields`
    fields = instance._meta.fields
    print(f"FIELDS:>>>>>>>> >>>> >>> > > > {fields}")
    for field in fields:
        if isinstance(field, FileField) and not field.name == "thumbnail":
            if not getattr(instance, field.name):
                # ignore empty fields
                print(
                    f"{field.name}ERROR >> NO FILE FIELDS FOUND >>>> ERROR >>> ERROR >>>ERROR"
                )
                continue

            # trigger conversion
            fieldfile = getattr(instance, field.name)
            print("VIDEO ENCODER: PREPARING TO RUN CONVERT_VIDEO")
            convert_video(fieldfile)


def convert_all_videos(app_label, model_name, object_pk):
    """
    Automatically converts all videos of a given instance.
    """
    # get instance
    Model = apps.get_model(app_label=app_label, model_name=model_name)
    instance = Model.objects.get(pk=object_pk)

    # search for `VideoFields`
    fields = instance._meta.fields
    for field in fields:
        if isinstance(field, VideoField):
            if not getattr(instance, field.name):
                # ignore empty fields
                continue

            # trigger conversion
            fieldfile = getattr(instance, field.name)
            convert_video(fieldfile)


def convert_video(fieldfile, force=False):
    """
    Converts a given video file into all defined formats.
    """
    print("VIDEO ENCODER: CONVERT_VIDEO TASK STARTED")
    instance = fieldfile.instance
    field = fieldfile.field

    with get_local_path(fieldfile) as source_path:
        encoder_backend = get_backend()

        signals.encoder_started.send(instance.__class__, instance=instance)
        for options in settings.VIDEO_ENCODING_FORMATS[encoder_backend.name]:
            video_format, created = Format.objects.get_or_create(
                object_id=instance.pk,
                content_type=ContentType.objects.get_for_model(instance),
                field_name=field.name,
                format=options["name"],
            )
            signals.format_started.send(Format, instance=instance, format=video_format)

            # do not reencode if not requested
            if video_format.file and not force:
                signals.format_finished.send(
                    Format,
                    instance=instance,
                    format=video_format,
                    result=signals.ConversionResult.SKIPPED,
                )
                continue

            try:
                _encode(source_path, video_format, encoder_backend, options)
            except VideoEncoderError:
                signals.format_finished.send(
                    Format,
                    instance=instance,
                    format=video_format,
                    result=signals.ConversionResult.FAILED,
                )
                # TODO handle with more care
                video_format.delete()
                continue
            signals.format_finished.send(
                Format,
                instance=instance,
                format=video_format,
                result=signals.ConversionResult.SUCCEEDED,
            )
        signals.encoder_finished.send(instance.__class__, instance=instance)


def _encode(
    source_path: str,
    video_format: Format,
    encoder_backend: BaseEncoderBackend,
    options: dict,
) -> None:
    """
    Encode video and continously report encoder progress.
    """
    # TODO do not upscale videos
    # TODO move logic to Format model

    with tempfile.NamedTemporaryFile(
        suffix="_{name}.{extension}".format(**options)
    ) as file_handler:
        target_path = file_handler.name

        # set progress to 0
        video_format.reset_progress()

        encoder = encoder_backend.encode(source_path, target_path, options["params"])
        while encoder:
            try:
                progress = next(encoder)
            except StopIteration:
                break
            video_format.update_progress(progress)

        # save encoded file
        print("VIDEO ENCODER: SAVING ENCODED FILE")
        filename = os.path.basename(source_path)
        # TODO remove existing file?
        video_format.file.save(
            "{filename}_{name}.{extension}".format(filename=filename, **options),
            File(open(target_path, mode="rb")),
        )

        video_format.update_progress(100)  # now we are ready
