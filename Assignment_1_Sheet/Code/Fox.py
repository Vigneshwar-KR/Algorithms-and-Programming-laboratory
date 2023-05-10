from Mammal import Mammal
from typing import Optional

class Fox (Mammal):
    
    def __init__(self, age: int , bite_force: float ) -> None:

        self._age=age
        self._bite_force = bite_force

    def hunt(self, prey_size:float) ->None:
        self.prey_size = prey_size

        if(self.prey_size < 5):
            print(f"\n The hunt is not worthwhile for the fox and the prey is too small")

        elif((2*self.prey_size ) > self._bite_force):
            print(f"\n The {self.__class__.__name__} cannot hunt the prey of size {self.prey_size} ")

        elif(self._bite_force > (2*self.prey_size)):
            print(f"\n The {self.__class__.__name__} was able to hunt the prey of size {self.prey_size} and ate it")

        
    def print (self) -> None:
        print (f"""\nThis Mammal is {self.__class__.__name__} of age {self._age} and has a bitte force of {self._bite_force}""")
        

# if __name__== "__main__":
#     l = Fox(10,50)
#     a = l.hunt(30)     

#     print(a)