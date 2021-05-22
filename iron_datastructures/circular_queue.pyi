from _queue_position import QueuePosition as QueuePosition
from linked_list import LinkedList as LinkedList
from typing import Generic, TypeVar

T = TypeVar("T")

class CircularQueue(Generic[T]):
    def __init__(self, maxSize: int) -> None: ...
    def __len__(self) -> int: ...
    def enQueue(self, item: T) -> None: ...
    def deQueue(self) -> T: ...
    def get(self, position: QueuePosition) -> T: ...
    def isEmpty(self) -> bool: ...
    def isFull(self) -> bool: ...
