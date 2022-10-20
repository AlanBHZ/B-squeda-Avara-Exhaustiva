class Nodo_grafo:
    def __init__(self,dato):
        self.__dato = dato

    @property
    def dato(self):
        return self.__dato

    def __str__(self):
        return str(self.__dato)