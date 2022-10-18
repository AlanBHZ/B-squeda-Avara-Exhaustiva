from nodo import Nodo
class Arbol:
  #Constructor
  def__init__(self,dato):
    self.raiz = Nodo(dato)
  ###########Funciones privadas###########
  #Agregar un nodo al árbol
  def __agregar(self,nodo,dato):
    if dato<nodo.dato:
      if nodo.izq is None:
        nodo.izq = Nodo(dato)
      else:
        self.__agregar(nodo.izq,dato)
    else:
      if dato.der is None: 
        nodo.der = Nodo(dato)
      else:
        self.__agregar(nodo.der,dato)

  #Recorrer árbol inorden      
  def __inorden(self,nodo):
    if nodo is not None:
      self.__inorden(nodo.izq)
      print(nodo.dato,end=", ")
      self.__inorden(nodo.derecha)
  #Recorrer árbol preorden    
  def __preorden(self,nodo):
    if nodo is not None: 
      print(nodo.dato,end=", ")
      self.__inorden(nodo.izq)
      self.__inorden(nodo.derecha)
      #Recorrer árbol postorden    
  def __postorden(self,nodo):
    if nodo is not None: 
      self.__inorden(nodo.izq)
      self.__inorden(nodo.derecha)
      print(nodo.dato,end=", ")

  def __busqueda_avara(self,nodo,busqueda):
    print("Hola")
  ###########Funciones publicas###########  
def agregar(self,dato): 
  self.__agregar(self.raiz,dato)
def inorden(self,dato):
  print("Recorrido In Orden del árbol: ")
  self.__inorden(self.raiz,dato)
  print(" ")  
def preorden(self,dato):
  print("Recorrido Pre Orden del árbol: ")
  self.__preorden(self.raiz,dato)
  print(" ")  
def postorden(self,dato):
  print("Recorrido Post Orden del árbol: ")
  self.__postorden(self.raiz,dato)
  print(" ")  
def busqueda_avara(self, busqueda):
  print("Busqueda")