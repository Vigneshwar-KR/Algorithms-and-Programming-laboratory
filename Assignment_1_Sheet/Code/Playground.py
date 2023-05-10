from Mammal import Mammal
from Leopard import Leopard
from Fox import Fox

if __name__== "__main__":

    Leopard_1 = Leopard(49,357)
    Leopard_2 = Leopard()

    Fox_1 = Fox(53,22)
    
    Leopard_1.set_lives_in_forest(True)
    Leopard_2.set_lives_in_forest(False)

    Fox_1.hunt(10)

    Animal_array = [Leopard_1,Leopard_2,Fox_1]

    
    for a in Animal_array:
        a.print()
    print("\n")
        
    for a in Animal_array:        
        for i in range(0,len(Animal_array)):
            print(Animal_array[i])
            if i!=Animal_array.index(a):
                a.meet(Animal_array[i])
        print("\n")


