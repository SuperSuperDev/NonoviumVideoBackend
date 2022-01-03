from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from nonovium_video_backend.videos.api.serializers import (
    PopulatedVideoPostSerializer,
    PopulatedVideoSerializer,
    VideoSerializer,
    VideoUploadSerializer,
)
from nonovium_video_backend.videos.models import Video, VideoPost


class VideoViewSet(viewsets.ViewSet):
    """
    API endpoint that allows videos to be viewed or !edited.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def list(self, request):
        """
        Return a list of all videos.
        """
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        print(
            f"request.user: {request.user}, request.auth: {request.auth}, request.data: {request.data}"
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Return a specific video by id, Returns video formats
        """
        queryset = Video.objects.all()
        video = get_object_or_404(queryset, id=pk)
        serializer = PopulatedVideoSerializer(video)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a video.
        """
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request):
    #     """
    #     Create a new video.
    #     """
    #     serializer = VideoSerializer(data=request.data)
    #     print(f'REQUEST DATA: {request.data}')
    #     # VideoFieldFile.file = request.data['file']
    #     # Video.file = VideoField(request.data['file'])
    #     # fieldData = request.data['title']
    #     # print(f'FILE: {file}')
    #     # print(f'FIELD DATA: {fieldData}')
    #     # print('CHECKING VALIDITY')
    #     if serializer.is_valid():
    #         print('VALID')
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def upload(self, request, pk=None):
    #     """
    #     Upload a video.
    #     """
    #     video = get_object_or_404(Video, id=pk)
    #     video.file = request.data['file']
    #     video.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        """
        Update a video.
        """
        video = get_object_or_404(Video, id=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a video.
        """
        video = get_object_or_404(Video, id=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned videos to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     return self.queryset()


class VideoUploadViewSet(viewsets.ViewSet):
    queryset = Video.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = VideoUploadSerializer

    def create(self, request):
        serializer = VideoUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=False)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
