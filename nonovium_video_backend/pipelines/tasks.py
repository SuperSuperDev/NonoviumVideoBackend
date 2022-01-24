import os

from django.core.files import File

from config import celery_app
from nonovium_video_backend.pipelines.models import VideoFile
from nonovium_video_backend.video_encoder.backends import get_backend
from nonovium_video_backend.video_encoder.tasks import convert_all_video_files

# from posixpath import basename


@celery_app.task(soft_time_limit=10000)
def convert_video_file_task(app_label, model_name, pk):
    get_uploaded_media_info(app_label, model_name, pk)
    return True


@celery_app.task(soft_time_limit=100)
def get_uploaded_media_info(app_label, model_name, pk):
    videoFile = VideoFile.objects.get(pk=pk)

    if not videoFile.file:  # no video file attached
        return print("NO VIDEO FILE FOUND")

    encoder_backend = get_backend()
    media_info = encoder_backend.get_media_info(videoFile.file.path)
    VideoFile.objects.filter(pk=pk).update(
        width=media_info["width"],
        height=media_info["height"],
        size=media_info["size"],
        duration=media_info["duration"],
    )
    return create_thumbnail(app_label, model_name, pk)


@celery_app.task(soft_time_limit=20)
def create_thumbnail(app_label, model_name, pk):
    videoFile = VideoFile.objects.get(pk=pk)
    if not videoFile.file:
        # no video file attached
        return print("NO VIDEO FILE FOUND")

    if videoFile.thumbnail:
        # thumbnail has already been generated
        return print("THUMBNAIL ALREADY GENERATED")
    print("GENERATING THUMBNAIL")
    encoder_backend = get_backend()
    thumbnail_path = encoder_backend.get_thumbnail(videoFile.file.path)
    filename = os.path.basename(str(pk) + ".png")

    try:
        with open(thumbnail_path, "rb") as file_handler:
            django_file = File(file_handler)
            videoFile.thumbnail.save(filename, django_file)
            videoFile.update_fields = ["thumbnail"]
    finally:
        os.unlink(thumbnail_path)

        return convert_all_video_files(app_label, model_name, pk)
