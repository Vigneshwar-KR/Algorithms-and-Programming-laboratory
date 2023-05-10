from typing import Optional
from Mammal import Mammal

class Leopard (Mammal):
    
    def __init__(self, age: Optional[int] = 0 , stomach_volume: Optional[int] = 49) -> None:
            self._stomach_volume = stomach_volume
            self._age = age

    def get_stomach_volume(self) -> int:
        return self._stomach_volume
        

    def print(self) -> None:
        print(f"""\nThis Mammal is {self.__class__.__name__} of age {self._age}, which has stomach volume of {self._stomach_volume}""")
        