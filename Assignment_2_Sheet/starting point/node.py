from __future__ import annotations
from typing import Optional
from shapes.shape import Shape


class Node:
    def __init__(self, content: Optional[Shape] = None) -> None:
        self._content: Optional[Shape] = content
        self._next: Optional[Node] = None

    def set_content(self, content :Shape) -> None:
        self._content = content
    
    def get_content(self) -> Optional[Shape]:
        return self._number

    def set_next(self, next: Node) -> None:
        self._next = next
    
    def get_next(self) -> Node:
        return self._next

        