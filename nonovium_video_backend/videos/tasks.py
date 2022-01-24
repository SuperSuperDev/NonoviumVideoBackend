import os

from django.core.files import File

from config import celery_app
from nonovium_video_backend.video_encoder.backends import get_backend
from nonovium_video_backend.video_encoder.tasks import convert_all_videos
from nonovium_video_backend.videos.models import Video

# from posixpath import basename


# from django.core.files.storage import default_storage
# from vidgear.gears import CamGear, WriteGear


# from .models import Video

# TODO Major refactoring work to be done on below code - possibly add to own celery task?
# @celery_app.task(soft_time_limit=10000)
# def encode_video(video_pk):
#     video_instance = Video.objects.get(pk=video_pk)
#     video_file = video_instance.file
#     video_path = video_file.path
#     stream = CamGear(source=video_path).start()
#     writer = WriteGear(
#         output_filename=default_storage.path(
#             os.path.join(
#                 "encoded_videos",
#                 f"{video_pk}_{video_file.name}",
#             )
#         ),
#         compression_mode=True,
#         logging=True,
#     )
#     while True:
#         frame = stream.read()
#         if frame is None:
#             break
#         writer.write(frame)
#     stream.stop()
#     writer.close()

#     ffmpeg_command_encode_mp4_360p = [
#         "-y",
#         "-i",
#         video_path,
#         "-vf",
#         "scale=-2:360",
#         "-movflags",
#         "faststart",
#         "-crf",
#         "17",
#         "-vcodec",
#         "h264",
#         "-acodec",
#         "aac",
#         "-strict",
#         "-2",
#         default_storage.path(
#             os.path.join(
#                 "encoded_videos",
#                 f"{video_pk}_360_{video_file.name}",
#             )
#         ),
#     ]
#     writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_360p)
#     print("Video encoder complete 2")

#     ffmpeg_command_encode_mp4_SD = [
#         "-y",
#         "-i",
#         video_path,
#         "-vf",
#         "scale=-2:720",
#         "-movflags",
#         "+faststart",
#         "-crf",
#         "17",
#         "-vcodec",
#         "h264",
#         "-acodec",
#         "aac",
#         "-strict",
#         "-2",
#         "-max_muxing_queue_size",
#         "1024",
#         default_storage.path(
#             os.path.join(
#                 "encoded_videos",
#                 f"{video_pk}_SD_{video_file.name}",
#             )
#         ),
#     ]

#     writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_SD)

#     ffmpeg_command_encode_mp4_HD = [
#         "-y",
#         "-i",
#         video_path,
#         "-vf",
#         "scale=-2:1080",
#         "-movflags",
#         "+faststart",
#         "-crf",
#         "17",
#         "-vcodec",
#         "h264",
#         "-acodec",
#         "aac",
#         "-strict",
#         "-2",
#         "-max_muxing_queue_size",
#         "1024",
#         default_storage.path(
#             os.path.join(
#                 "encoded_videos",
#                 f"{video_pk}_HD_{video_file.name}",
#             )
#         ),
#     ]

#     writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_HD)

#     video_4K_output_path = default_storage.path(
#         os.path.join(
#             "encoded_videos",
#             f"{video_pk}_4K_{video_file.name}",
#         ))

#     ffmpeg_command_encode_mp4_4K = [
#         "-y",
#         "-i",
#         video_path,
#         "-vf",
#         "scale=-2:2160",
#         "-movflags",
#         "+faststart",
#         "-crf",
#         "17",
#         "-vcodec",
#         "h264",
#         "-acodec",
#         "aac",
#         "-strict",
#         "-2",
#         "-max_muxing_queue_size",
#         "1024",
#         video_4K_output_path,
#     ]


#     writer.execute_ffmpeg_cmd(ffmpeg_command_encode_mp4_4K)

#     #video_instance.video_360 = File(open(video_4K_output_path, "rb"))

#     video_instance.video_360 = {
#         basename(video_4K_output_path),
#         File(open(video_4K_output_path, "rb"))
#         }
#     video_instance.save(update_fields=["video_360"])
# video_instance.video_360.save(basename(video_4K_output_path), content=File(open(video_4K_output_path, "rb")))

# print("Video encoder complete 4")
# return True


@celery_app.task(soft_time_limit=10000)
def convert_video_task(app_label, model_name, pk):
    create_thumbnail(app_label, model_name, pk)
    return True


@celery_app.task(soft_time_limit=20)
def create_thumbnail(app_label, model_name, pk):
    video = Video.objects.get(pk=pk)
    if not video.file:
        # no video file attached
        return print("NO VIDEO FILE FOUND")

    if video.thumbnail:
        # thumbnail has already been generated
        return print("THUMBNAIL ALREADY GENERATED")
    print("GENERATING THUMBNAIL")
    encoder_backend = get_backend()
    thumbnail_path = encoder_backend.get_thumbnail(video.file.path)
    filename = os.path.basename(str(pk) + ".png")

    try:
        with open(thumbnail_path, "rb") as file_handler:
            django_file = File(file_handler)
            video.thumbnail.save(filename, django_file)
            video.update_fields = ["thumbnail"]
            print("VIDEO THUMBNAIL COMPLETE")
    finally:
        os.unlink(thumbnail_path)
        print("PREPARING TO RUN CONVERT ALL VIDEOS")

        return convert_all_videos(app_label, model_name, pk)
