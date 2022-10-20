from arista import AristaNoDirigida
from nodo_grafo import Nodo_grafo


class Grafo:
    def __init__(self):
        self.__aristas = []
        self.__ady = []  # {}

    def agregar_arista(self, arista: AristaNoDirigida):
        if arista not in self.__aristas:
            self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])

    def get_lista_ady(self):
        for arista in self.__aristas:   
            n1 = arista.get_nodo1()
            n2 = arista.get_nodo2()
            self.agregar_ady(n1, n2)
        return self.__ady

    def agregar_ady(self, n1: Nodo_grafo, n2: Nodo_grafo):
        #if n1 in self.__ady:
        #    self.__ady.append([n2])
        #else:
        #    self.__ady[n1] = [[n2]]
        if n1 in self.__ady:
            self.__ady.append([n2])
        else: 
            self.__ady[n1] = [[n2]]
