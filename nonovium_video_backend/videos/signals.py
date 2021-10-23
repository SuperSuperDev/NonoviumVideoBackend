# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # from .tasks import create_thumbnail as create_thumbnail_task
# from django_rq import enqueue
# from nonovium_video_backend.video_encoder import tasks

# from .models import Video
# from .tasks import convert_video_task

# from .tasks import encode_video

# @receiver(post_save, sender=Video)
# def encode_video_on_save(sender, instance, **kwargs):
#     encode_video.delay(instance.pk)


# @receiver(post_save, sender=Video)
# def convert_video(sender, instance, **kwargs):
#     enqueue(
#         tasks.convert_all_videos,
#         instance._meta.app_label,
#         instance._meta.model_name,
#         instance.pk,
#     )


# @receiver(post_save, sender=Video)
# def create_thumbnail(sender, instance, **kwargs):
#     create_thumbnail_task.delay(instance.pk)

# @receiver(post_save, sender=Video)
# def convert_video(sender, instance, **kwargs):
#     # enqueue(tasks.convert_all_videos,
#     #         instance._meta.app_label,
#     #         instance._meta.model_name,
#     #         instance.pk)

#     # tasks.convert_all_videos,
#     # instance._meta.app_label,
#     # instance._meta.model_name,
#     # instance.pk
#     convert_video_task.delay(
#     instance._meta.app_label,
#     instance._meta.model_name,
#     instance.pk
#     )
