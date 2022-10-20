from nodo_grafo import Nodo_grafo

class Arista:
    def __init__(self, n1:Nodo_grafo, n2:Nodo_grafo, peso):
        self.__par = [n1, n2]
        self.__peso = peso

    def dirigido(self) -> bool:
        return False

    def ponderada(self) -> bool:
        return False

    def get_par(self) -> list:
        return self.__par

    def __str__(self) -> str:
        return f"({self.get_par()[0]} ----- {self.__peso} -----> {self.get_par()[1]}))"

    def __eq__(self, __o: object) -> bool:
        if self.get_par()[0] == __o.get_par()[0] and self.get_par()[1] == __o.get_par()[1]:
            return True
        else:
            return False
class AristaNoDirigida(Arista):
    def __init__(self, n1: Nodo_grafo, n2: Nodo_grafo, peso):
        super().__init__(n1, n2, peso)
    def dirigido(self)->bool:
        return False
    def get_nodo1(self)->Nodo_grafo:
        return self.get_par()[0]    
    def get_nodo2(self)->Nodo_grafo:
        return self.get_par()[1]
    def __str__(self) -> str:
        return f"({self.get_nodo1()} ----- {self.__peso} -----> {self.get_nodo2()}))"
        
#https://www6.uniovi.es/usr/cesar/Uned/EDA/Apuntes/TAD_apUM_07.pdf