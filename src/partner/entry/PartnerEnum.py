from enum import IntEnum


class MemoryTypeEnum(IntEnum):
    SHORT_TERM = 1
    MEDIUM_TERM = 2
    LONG_TERM = 3
    SHORT_COUNT = 30

class DelEnum(IntEnum):
    NO=1
    YES=0

class MessageType(IntEnum):
    AI=1
    HUMAN=2
