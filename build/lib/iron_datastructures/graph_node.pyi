from typing import Optional, TypeVar

T = TypeVar('T')

class Node:
    data: Optional[T]
    connections: list[int]
    visited: bool = ...
    def __init__(self, data: Optional[T], connections: list[int]=...) -> None: ...
    def clone(self) -> Node[T]: ...
