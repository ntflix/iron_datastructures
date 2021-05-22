from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class LinkedListNode(Generic[T]):
    data: T
    nextNode: Optional[LinkedListNode[T]]
    def __init__(
        self, data: T, nextNode: Optional[LinkedListNode[T]] = ...
    ) -> None: ...
    def clone(self) -> LinkedListNode[T]: ...
