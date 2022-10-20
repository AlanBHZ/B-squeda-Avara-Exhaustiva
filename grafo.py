from arista import Arista

class Grafo:
    def __init__(self):
        self.__aristas = []

    def agregar_arista(self, arista: Arista):
        self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])