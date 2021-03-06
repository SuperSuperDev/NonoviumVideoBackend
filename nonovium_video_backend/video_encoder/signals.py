import enum

from django.dispatch import Signal


class ConversionResult(enum.Enum):
    SUCCEEDED = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


encoder_started = Signal()
encoder_finished = Signal()

format_started = Signal()
format_finished = Signal()
