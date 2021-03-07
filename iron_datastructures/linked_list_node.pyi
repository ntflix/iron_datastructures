from typing import Optional, TypeVar

T = TypeVar('T')

class LinkedListNode:
    data: T
    nextNode: Optional[LinkedListNode[T]]
    def __init__(self, data: T, nextNode: Optional[LinkedListNode[T]]=...) -> None: ...
    def clone(self) -> LinkedListNode[T]: ...
