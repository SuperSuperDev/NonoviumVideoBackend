from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
# from drf_yasg import openapi as openapi
# from drf_yasg.utils import swagger_auto_schema

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

    # @swagger_auto_schema(
    #     manual_parameters=[
    #         openapi.Parameter(
    #             name="video_file",
    #             in_=openapi.IN_FORM,
    #             type=openapi.TYPE_FILE,
    #             required=True,
    #             description="The video file to upload.",
    #         ),
    #         openapi.Parameter(
    #             name="title",
    #             in_=openapi.IN_FORM,
    #             type=openapi.TYPE_STRING,
    #             required=False,
    #             description="title",
    #         ),
    #     ],
    #     tags=["VideoFile"],
    #     operation_summary="Upload a video file.",
    #     operation_description="Upload a video file a start base encoding",
    #     responses={
    #         201: openapi.Response("response description", VideoFileSerializer),
    #         401: "bad request",
    #     },
    # )
    def create(self, request):
        """
        Create a video.
        """
        serializer = VideoFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def create_video_file(self, request):
    #     """
    #     Create a
    #             description="Video file to upload",
    #         )
    #     ]
    # )
    # def create_video_file(self, request):
    #     """
    #     Create a
    #         )

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
