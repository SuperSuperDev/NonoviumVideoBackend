from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from nonovium_video_backend.videos.models import Video, VideoPost

from .serializers import PopulatedVideoPostSerializer, VideoSerializer


class VideoListView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    API endpoint that allows videos to be viewed or !edited.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned videos to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        return self.queryset()


class VideoPostListView(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):

    queryset = VideoPost.objects.all()
    serializer_class = PopulatedVideoPostSerializer

    def get_queryset(self):
        # return self.queryset.filter(user=self.request.user)
        return self.queryset

    # def get_queryset(self):
    #     return self.queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoPostDetailView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = VideoPost.objects.all()
    serializer_class = PopulatedVideoPostSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwarks["post_id"])


class VideoPostViewSet(viewsets.ViewSet):
    """
    API endpoint that allows videos to be viewed or edited.
    """

    queryset = VideoPost.objects.all()
    serializer_class = PopulatedVideoPostSerializer

    def list(self, request):
        # queryset = self.queryset.filter(user=self.request.user)
        queryset = VideoPost.objects.all()
        serializer = PopulatedVideoPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = VideoPost.objects.all()
        video_post = get_object_or_404(queryset, post_id=pk)
        serializer = PopulatedVideoPostSerializer(video_post)
        return Response(serializer.data)

    def update(self, request, post_id=None):
        queryset = self.queryset.filter(user=self.request.user)
        video_post = get_object_or_404(queryset, post_id=self.post_id)
        serializer = PopulatedVideoPostSerializer(video_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
