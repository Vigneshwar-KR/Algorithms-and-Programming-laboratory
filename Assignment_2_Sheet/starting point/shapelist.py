from typing import Protocol
from shapes.shape import Shape


class ShapeList(Protocol):
    def add(self, shape: Shape) -> None:
        pass

    def insert(self, shape: Shape, index: int) -> None:
        pass

    def remove_last(self) -> None:
        pass

    def remove(self, index: int) -> None:
        pass

    def clear(self) -> None:
        pass

    def get_shape(self, index: int) -> Shape:
        pass

    def get_size(self) -> int:
        pass

    def sort(self) -> None:
        pass

    def print(self) -> None:
        pass
