from __future__ import annotations
import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y

    def distance_to(self, other_point: Point) -> float:
        distance: float = math.sqrt(
            pow(self._x - other_point.get_x(), 2)
            + pow(self._y - other_point.get_y(), 2)
        )
        return distance

    def __str__(self) -> str:
        return f"(x: {self._x} | y: {self._y})"
