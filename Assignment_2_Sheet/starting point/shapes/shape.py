from abc import ABC, abstractmethod
from .point import Point


class Shape(ABC):
    def __init__(self, center: Point) -> None:
        self._center = center

    @abstractmethod
    def scale(self, scaling_factor: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calc_peri(self) -> float:
        pass

    def move_to(self, new_center: Point) -> None:
        self._center = new_center
