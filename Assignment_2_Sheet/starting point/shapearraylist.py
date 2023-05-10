from shapelist import ShapeList
from typing import Any
import numpy as np

from shapes.shape import Shape
from shapes.circle import Circle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.point import Point


class ShapeArrayList(ShapeList):
    def __init__(self) -> None:
        self._max_size: int = 4
        self._internal_array: np.ndarray[Any, Any] = np.empty(self._max_size, dtype=object)
        self._element_count: int = 0
        self._str = ""

    # helper functions

    def _double_internal_array(self) -> None:
        self._max_size *= 2
        self._internal_array.resize(self._max_size)
        self._internal_array[self._internal_array == 0] = None

    def _halve_internal_array(self) -> None:
        self._max_size = int(self._max_size / 2)
        self._internal_array.resize(self._max_size)

    def add(self,shape:Shape)->None:
        if self._element_count==self._max_size:
          self._double_internal_array()
        self._internal_array[self._element_count]=shape
        self._element_count+=1


    def insert(self, shape: Shape, index: int) -> None:
        self._index = index
        if self._index<0:
            raise IndexError["Invalid negative index"]
        elif self._index >self._element_count:
            raise IndexError["Out of Index"]
        else:
            if self._index==self._element_count:
                self.add(shape) 
            else:
                if self._element_count==self._max_size:
                   self._double_internal_array()
                   
                temp=np.empty(len(self._internal_array),dtype=object)
                for i in range(0,len(self._internal_array)):
                    temp[i]=self._internal_array[i]
                                
                self._internal_array[index]= shape

                for i in range(self._index,self._element_count):
                    self._internal_array[i+1]=temp[i]
                self._element_count +=1
    
    def remove_last(self)->None:
        self._internal_array[self._element_count-1]=0
        self._element_count-=1
        if self._element_count<=(self._max_size/2):
            self._halve_internal_array()

    def remove(self,index:int)->None:
        self._index = index
        if self._index<0:
            raise IndexError("Invalid negative index")
        elif self._index >=self._element_count:
            raise IndexError("Out of Index")
        else:
            if self._index==self._element_count-1:
                self.remove_last()
            else:
                size = len(self._internal_array)
                temp=np.zeros(size,dtype=object)
                for i in range(0,size):
                    temp[i]=self._internal_array[i]


                for i in range(self._index,self._element_count-1):
                    self._internal_array[i]=temp[i+1]
                self._element_count-=1
                if self._element_count<=(self._max_size/2):
                    self._halve_internal_array()

    def clear(self):
        self.__init__()

    def get_shape(self,index:int)->Shape:
        if index<0:
            raise IndexError("Invalid negative index")
        if index>=self._element_count:
            raise IndexError("Out of Index")
        return self._internal_array[index]

    def get_size(self)->int:
        return self._element_count

    def sort(self)->None:
        #INSERTION SORT
        current = self._internal_array
        for j in range(0, self._element_count):
            target = current[j]
            k = j - 1
            while k >= 0 and target.calculate_area()< current[k].calculate_area():
                current[k + 1] = current[k]
                k -= 1
            current[k + 1] = target


    
    def print(self)->str:
        self._str=""
        for i in range(0,self._element_count):
            self._str +=self._internal_array[i].__str__()+"\n"
        return self._str


if __name__=="__main__":

    point_1 = Point(4, 6)
    point_2 = Point(21, 10.5)
    point_3 = Point(-6.2, 11)

    c = Circle(point_1, 3)
    t = Triangle(point_2, 5)
    s = Square(point_3, 2)

    shapeList: list[Shape] = [c, t, s]
    list = shapeList

    sample=ShapeArrayList()
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
# 3 Use the helper functions to double or halve the size of the internal array if it is helpful
