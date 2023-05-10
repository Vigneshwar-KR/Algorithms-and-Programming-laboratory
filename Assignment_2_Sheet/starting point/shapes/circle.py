import math
from .point import Point
from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, center: Point, radius: float) -> None:
        self._radius = radius
        super().__init__(center)

    def scale(self, scaling_factor: float) -> None:
        self._radius *= scaling_factor

    def __str__(self) -> str:
        return f"Circle at: {self._center} with the radius: {self._radius} and area: {self.calculate_area(): .2f}"

    def calculate_area(self) -> float:
        return math.pi * self._radius * self._radius

    def calc_peri(self) -> float:
        return math.pi * self._radius * 2


if __name__ == "__main__":
    point1 = Point(22, 11)
    point2 = Point(11, 4)
    circle1 = Circle(point1, 2)
    circle1.move_to(point2)

    print(circle1)
