from typing import TypeVar

T = TypeVar('T')

class Stack:
    def pop(self) -> T: ...
    def peek(self) -> T: ...
    def push(self, item: T) -> None: ...
    def isEmpty(self) -> bool: ...
    def __len__(self) -> int: ...