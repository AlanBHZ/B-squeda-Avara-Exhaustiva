from nodo import Nodo
class Arbol:
  #Constructor
  def __init__(self,letra,peso):
    self.raiz = Nodo(letra,peso)

  ###########Funciones privadas###########
  #Agregar un nodo al árbol
  def __agregar(self,nodo,letra,peso):
    if letra != self.raiz.letra:
      if letra<nodo.letra:
        if nodo.izq is None:
          nodo.izq = Nodo(letra,peso)
        else:
          self.__agregar(nodo.izq,letra,peso)
      else:
        if nodo.der is None: 
          nodo.der = Nodo(letra,peso)
        else:
          self.__agregar(nodo.der,letra,peso)

  #Recorrer árbol inorden      
  def __inorden(self,nodo):
    if nodo is not None:
      self.__inorden(nodo.izq)
      print(nodo.letra,end=", ")
      self.__inorden(nodo.der)
  #Recorrer árbol preorden    
  def __preorden(self,nodo):
    if nodo is not None: 
      print(nodo.letra,end=", ")
      self.__inorden(nodo.izq)
      self.__inorden(nodo.der)
  #Recorrer árbol postorden    
  def __postorden(self,nodo):
    if nodo is not None: 
      self.__inorden(nodo.izq)
      self.__inorden(nodo.der)
      print(nodo.letra,end=", ")

  def __busqueda_avara(self,nodo,busqueda):
    print("Hola")

  ###########Funciones publicas###########  
  def agregar(self,letra,peso): 
    self.__agregar(self.raiz,letra,peso)
  def inorden(self):
    print("Recorrido In Orden del árbol: ")
    self.__inorden(self.raiz)
    print(" ")  
  def preorden(self):
    print("Recorrido Pre Orden del árbol: ")
    self.__preorden(self.raiz)
    print(" ")  
  def postorden(self):
    print("Recorrido Post Orden del árbol: ")
    self.__postorden(self.raiz)
    print(" ")  
  def busqueda_avara(self, busqueda):
    print("Busqueda")