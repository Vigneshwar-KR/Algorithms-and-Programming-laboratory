from .point import Point
from shapes.shape import Shape


class Square(Shape):
    def __init__(self, center: Point, side_length: float) -> None:
        self._side_length = side_length
        super().__init__(center)

    def scale(self, scaling_factor: float) -> None:
        self._side_length *= scaling_factor

    def __str__(self) -> str:
        return f"Square at: {self._center} with the sidelength: {self._side_length} and area: {self.calculate_area(): .2f}"

    def calculate_area(self) -> float:
        return self._side_length**2

    def calc_peri(self) -> float:
        return self._side_length * 4
