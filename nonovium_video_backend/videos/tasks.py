import os

from django.core.files.storage import default_storage
from vidgear.gears import CamGear, WriteGear

from config import celery_app

# from video_encoding.backends import get_backend
from .models import Video


@celery_app.task(soft_time_limit=10000)
def encode_video(video_pk):
    video_instance = Video.objects.get(pk=video_pk)
    video_file = video_instance.file
    video_path = video_file.path
    stream = CamGear(source=video_path).start()
    writer = WriteGear(
        output_filename=default_storage.path(
            os.path.join(
                "encoded_videos",
                f"{video_pk}_{video_file.name}",
            )
        ),
        compression_mode=True,
        logging=True,
    )

    while True:
        frame = stream.read()

        if frame is None:
            break

        writer.write(frame)

    stream.stop()

    writer.close()
    ffmpeg_command_encode_mp4_360p = [
        "-y",
        "-i",
        video_path,
        "-vf",
        "scale=-2:360",
        "-movflags",
        "faststart",
        "-crf",
        "17",
        "-vcodec",
        "h264",
        "-acodec",
        "aac",
        "-strict",
        "-2",
        default_storage.path(
            os.path.join(
                "encoded_videos",
                f"{video_pk}_360_{video_file.name}",
            )
        ),
    ]
    writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_360p)
    print("Video encoding complete 2")

    ffmpeg_command_encode_mp4_SD = [
        "-y",
        "-i",
        video_path,
        "-vf",
        "scale=-2:720",
        "-movflags",
        "+faststart",
        "-crf",
        "17",
        "-vcodec",
        "h264",
        "-acodec",
        "aac",
        "-strict",
        "-2",
        "-max_muxing_queue_size",
        "1024",
        default_storage.path(
            os.path.join(
                "encoded_videos",
                f"{video_pk}_SD_{video_file.name}",
            )
        ),
    ]

    writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_SD)


# @celery_app.task()
# def create_thumbnail(video_pk):
#     video = Video.objects.get(pk=video_pk)
#     if not video.file:
#     # no video file attached
#         return print('NO VIDEO FILE FOUND')

#     if video.thumbnail:
#     # thumbnail has already been generated
#         return print('THUMBNAIL ALREADY GENERATED')
#     print('GENERATING THUMBNAIL')
#     encoding_backend = get_backend()
#     thumbnail_path = encoding_backend.get_thumbnail(video.file.path)
#     filename = os.path.basename(self.url),

#     try:
#         with open(thumbnail_path, 'rb') as file_handler:
#             django_file = File(file_handler)
#             video.thumbnail.save(filename, django_file)
#             video.save()
#     finally:
#         os.unlink(thumbnail_path)
