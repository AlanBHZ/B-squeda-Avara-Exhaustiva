class Nodo_grafo:
    def __init__(self,dato):
        self.__dato = dato

    @property
    def dato(self):
        return self.__dato

    def __str__(self):
        return str(self.__dato)
    
    def __eq__(self, __o: object) -> bool:
        if self.__dato == __o.dato:
            return True
        else: 
            return False
    
    def __hash__(self) -> int:
        return hash(self.__dato)        