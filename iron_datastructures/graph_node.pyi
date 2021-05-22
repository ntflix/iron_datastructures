from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class Node(Generic[T]):
    data: Optional[T]
    connections: list[int]
    visited: bool = ...
    def __init__(self, data: Optional[T], connections: list[int] = ...) -> None: ...
    def clone(self) -> Node[T]: ...
