class VideoEncoderError(Exception):
    pass


class FFmpegError(VideoEncoderError):
    def __init__(self, *args, **kwargs):
        self.msg = args[0]
        super(VideoEncoderError, self).__init__(*args, **kwargs)


class InvalidTimeError(VideoEncoderError):
    pass
