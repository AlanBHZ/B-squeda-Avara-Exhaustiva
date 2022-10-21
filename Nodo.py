class Nodo:
  def __init__(self,letra:str,peso):
    self.letra = letra
    self.peso = peso
    self.izq = None
    self.der = None