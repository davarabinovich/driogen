
from enum import Enum


class NonPhysicalBatchSizeError(Exception):
    def __init__(self):
        super().__init__('Non-physical item cannot have batch size attribute')


class BatchSize(Enum):
    UNIQUE = 0,
    SERIES = 1,
    MASS = 2

    def is_batch(self):
        result: bool = (self.value >= BatchSize.SERIES.value)
        return result

    def is_limited(self):
        result: bool = (self.value <= BatchSize.SERIES.value)
        return result


class Kind(Enum):
    PHYSICAL_ITEM = 0,
    PROGRAM = 1,
    TECH_PROCESS = 2

    def is_physical(self):
        result: bool = (self.value == Kind.PHYSICAL_ITEM)
        return result


class Item:
    def __init__(self, kind: Kind, batch_size: BatchSize | None = BatchSize.UNIQUE):
        self._kind: Kind = kind
        if not kind.is_physical() and batch_size is not None:
            raise NonPhysicalBatchSizeError

    @property
    def kind(self):
        return self._kind


class Element(Item):
    def __init__(self, kind: Kind):
        super().__init__(kind)

