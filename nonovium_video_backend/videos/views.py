from django.views.generic import CreateView

from .models import Video


class VideoFormView(CreateView):
    model = Video
    fields = ("file",)

    success_url = "/"
    template_name = "video_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VideoFormView, self).get_context_data(*args, **kwargs)
        context["videos"] = Video.objects.all()
        return context


video_form_view = VideoFormView.as_view()
