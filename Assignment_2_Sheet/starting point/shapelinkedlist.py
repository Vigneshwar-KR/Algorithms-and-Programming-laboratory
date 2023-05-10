from node import Node
from shapelist import ShapeList
from typing import Any
import numpy as np 

from shapes.shape import Shape
from shapes.circle import Circle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.point import Point

class ShapeLinkedList(ShapeList):
    # def __init__(self) -> None:
    #     self._head: Node = Node()
    #     self._cursor: Node = self._head
    #     self._size: int = 0

    def __init__(self) -> None:
        self._head: Node = None
        self._cursor: Node = self._head
        self._size: int = 0
        self._str = ""


    def add(self, shape:Shape) -> None:
        if self._head is None:
            self._head = Node(shape)
            self._head._next = None
            self._cursor = self._head
            self._size +=1

        else:
            self._cursor = self._head
            while self._cursor._next is not None:
                self._cursor = self._cursor._next
            self._cursor._next = Node(shape)
            self._size +=1


    def insert(self, shape: Shape, index: int) -> None:
        self._index = index
        if self._index < 0:
            raise IndexError("Invalid negative index")
        elif self._index > self._size:
            raise IndexError["Out of Index"]   
        elif self._index == 0:
            self._cursor = self._head
            self._head = Node(shape)
            self._head._next = self._cursor
            self._size += 1
        elif self._index  == self._size:
            self.add(shape)
        else:
            k = 0
            self._cursor = self._head
            while k != index - 1:
                self._cursor = self._cursor._next
                k += 1

            temp = self._cursor._next
            self._cursor._next = Node(shape)
            self._cursor = self._cursor._next
            self._cursor._next = temp
            self._size += 1

    def remove_last(self) -> None:
        if self._size == 0:
            raise IndexError("EmptyList")

        self._cursor = self._head
        while self._cursor._next._next is not None:
            self._cursor = self._cursor._next

        self._cursor._next = None
        self._size -= 1

    def remove(self, index: int) -> None:
        self._index = index
        if self._index >= self._size:
            raise IndexError("Invalid negative index")

        elif self._index < 0:
            raise IndexError("Out of Index")

        elif self._index == self._size - 1:
            self.remove_last()

        elif self._index == 0:
            self._head = self._head._next
            self._size -= 1

        else:
            k = 0
            self._cursor = self._head
            while k != index - 1:
                self._cursor = self._cursor._next
                k += 1

            self._cursor._next = self._cursor._next._next
            self._size -= 1

    def clear(self) -> None:
        self.__init__()

    def get_shape(self, index: int) -> Shape:
        self._index = index
        if self._index >= self._size:
            raise IndexError('Out of index')
        elif self._index < 0:
            raise IndexError("Invalid negative index")
        elif index == 0:
            return self._head._content
        else:
            k = 0
            self._cursor = self._head
            while (k != index):
                self._cursor = self._cursor._next
                k += 1

            return self._cursor._content

    def get_size(self) -> int:
        return self._size

    def sort(self) -> None:
        #Bubble Sort
        if self._head is None:
            raise IndexError("EmptyList")
        while True:
            swap : bool = False
            self._cursor = self._head
            while self._cursor._next is not None:
                if self._cursor._content.calculate_area() > self._cursor._next._content.calculate_area():
                    swap = True
                    self._cursor._content, self._cursor._next._content = self._cursor._next._content , self._cursor._content
                self._cursor = self._cursor._next
            if swap is False:
                break



    def print(self) -> str:
        self._cursor = self._head
        self._str = ""
        while self._cursor is not None:
            self._str += (self._cursor._content.__str__()) + "\n"
            self._cursor = self._cursor._next

        return self._str+"\n"

# ToDo
# 1 assign useful values in constructor
# 2 make sure the protocol is inherited correct
if __name__=="__main__":
    # def create_shape() -> list[Shape]:
    point_1 = Point(4, 6)
    point_2 = Point(21, 10.5)
    point_3 = Point(-6.2, 11)

    c = Circle(point_1, 3)
    t = Triangle(point_2, 5)
    s = Square(point_3, 2)

    shapeList: list[Shape] = [c, t, s]
    list = shapeList

    sample = ShapeLinkedList()
    for i in list:
        sample.add(i)

    print(sample.print())
    
    sample.sort()
    print(sample.print())

    point_4 = Point(3.7, 5.5)
    c_2 = Circle(point_4,2)
    sample.insert(c_2,2)
    print(sample.print())

    t_2 = Triangle(point_4, 3)
    sample.insert(t_2,3)
    print(sample.print())
    
    s_2 = Square(point_4, 5)
    s_2 = sample.insert(s_2,5)
    print(sample.print())
    sample.sort()

    print(sample.print())
    sample.remove_last()
    sample.remove(0)
    print(sample.get_size())
    print(sample.print())





# ToDo
# 1 assign usefull values in constructor
# 2 make sure the protocol is inherited correct
