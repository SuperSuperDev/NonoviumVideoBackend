from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets

# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from nonovium_video_backend.pipelines.api.serializers import (  # PopulatedVideoFileSerializer,
    VideoFileSerializer,
    VideoFileUploadSerializer,
)
from nonovium_video_backend.pipelines.models import VideoFile

# from rest_framework.viewsets import GenericViewSet


class VideoFileViewSet(viewsets.ViewSet):
    """
    API endpoint that allows videos to be viewed or !edited.
    """

    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerializer

    def list(self, request):
        """
        Return a list of all videos.
        """
        queryset = VideoFile.objects.all()
        serializer = VideoFileSerializer(queryset, many=True)
        print(
            f"request.user: {request.user}, request.auth: {request.auth}, request.data: {request.data}"
        )
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     """
    #     Return a specific video by id, Returns video formats
    #     """
    #     queryset = VideoFile.all()
    #     videoFile = get_object_or_404(queryset, id=pk)
    #     serializer = VideoFileSerializer(videoFile)
    #     return Response(serializer.data)

    def create(self, request):
        """
        Create a video.
        """
        serializer = VideoFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request):
    #     """
    #     Create a new video.
    #     """
    #     serializer = VideoFileSerializer(data=request.data)
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
        videoFile = get_object_or_404(VideoFile, id=pk)
        serializer = VideoFileSerializer(videoFile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a video.
        """
        videoFile = get_object_or_404(VideoFile, id=pk)
        videoFile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned videos to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     return self.queryset()


class VideoFileUploadViewSet(viewsets.ViewSet):
    queryset = VideoFile.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = VideoFileUploadSerializer

    def create(self, request):
        serializer = VideoFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=False)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class VideoPostListView(
#     ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
# ):

#     queryset = VideoPost.objects.all()
#     serializer_class = PopulatedVideoPostSerializer

#     def get_queryset(self):
#         # return self.queryset.filter(user=self.request.user)
#         return self.queryset

#     # def get_queryset(self):
#     #     return self.queryset()

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class VideoPostDetailView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
#     queryset = VideoPost.objects.all()
#     serializer_class = PopulatedVideoPostSerializer

#     def get_queryset(self):
#         return self.queryset.filter(post_id=self.kwarks["post_id"])


# class VideoPostViewSet(viewsets.ViewSet):
#     """
#     API endpoint that allows videos to be viewed or edited.
#     """

#     queryset = VideoPost.objects.all()
#     serializer_class = PopulatedVideoPostSerializer

#     def list(self, request):
#         # queryset = self.queryset.filter(user=self.request.user)
#         queryset = VideoPost.objects.all()
#         serializer = PopulatedVideoPostSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = VideoPost.objects.all()
#         video_post = get_object_or_404(queryset, post_id=pk)
#         serializer = PopulatedVideoPostSerializer(video_post)
#         return Response(serializer.data)

#     def update(self, request, post_id=None):
#         queryset = self.queryset.filter(user=self.request.user)
#         video_post = get_object_or_404(queryset, post_id=self.post_id)
#         serializer = PopulatedVideoPostSerializer(video_post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
