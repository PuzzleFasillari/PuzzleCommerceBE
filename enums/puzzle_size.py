from enum import Enum


class PuzzleSize(Enum):
    SMALL = ("small", 100)
    MEDIUM = ("medium", 500)
    LARGE = ("large", 1000)
    EXTRA_LARGE = ("extra_large", 2000)

    def __init__(self, label, size):
        self._label = label
        self._size = size

    @property
    def label(self):
        return self._label

    @property
    def size(self):
        return self._size

