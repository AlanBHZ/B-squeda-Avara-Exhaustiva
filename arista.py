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
        return f"(Nodo: {self.get_par()[0]} <----- {self.__peso} -----> (Nodo: {self.get_par()[1]}))"



#https://www6.uniovi.es/usr/cesar/Uned/EDA/Apuntes/TAD_apUM_07.pdf