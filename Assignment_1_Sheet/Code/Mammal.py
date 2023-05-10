from __future__ import annotations
from abc import ABC, abstractmethod

class Mammal(ABC):
    
    _lives_in_forest: bool  = True
    
    def __init__(self, age:int) -> None:
        self._age=age
        
    def get_lives_in_forest(self) -> bool:
        return self._lives_in_forest

    def set_lives_in_forest(self,lives_in_forest: bool) -> None:
        self._lives_in_forest = lives_in_forest
    
    def meet(self,animal: Mammal) -> None:
        if (self._lives_in_forest == animal.get_lives_in_forest()):
            print("The animals meet")

        else:
            print("The animals don't meet")

    @abstractmethod
    def print (self) -> None:
        pass

    
    
# if __name__== "__main__":
#     Leopard= Mammal(18,True)
#     Rat= Mammal(4,False)
#     a= Leopard.meet(Rat)

#     print(a)

        