class Nodo:
  def __init__(self,dato):
    self.dato = dato #será el valor almacenado en el nodo.
    self.anterior = None #referenciado al nodo anterior en la lista doblemente enlazada.
    self.siguiente = None #nodo siguiente en la lista doblemente enlazada.
