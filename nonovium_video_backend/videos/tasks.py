import os

from vidgear.gears import CamGear, WriteGear

from config import celery_app

# from django.core.files import File
# from video_encoding.backends import get_backend
from .models import Video

# import cv2


@celery_app.task
def encode_video(video_pk):
    video_instance = Video.objects.get(pk=video_pk)
    video_file = video_instance.file
    stream = CamGear(source=video_file.path).start()
    writer = WriteGear(
        output_filename=os.path.join(
            os.path.dirname(__file__),
            "media/encoded_videos",
        ),
        compression_mode=True,
    )

    while True:
        frame = stream.read()

        if frame is None:
            break

        writer.write(frame)

    #     cv2.imshow("Output Frame", frame)
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord("q"):
    #         break
    # cv2.destroyAllWindows()

    stream.stop()
    writer.close()


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
