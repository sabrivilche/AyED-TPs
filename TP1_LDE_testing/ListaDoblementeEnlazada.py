from Nodos import Nodo
class ListaDobleEnlazada:
  def __init__(self):
    self.cabeza = None
    self.cola = None
    self.tamanio = 0

  def vacia(self):
      return self.cabeza == None
  def agregar_al_final(self,item):
    if self.vacia():
      self.cabeza = self.cola = Nodo(item)
    else:
      aux_final = self.cola
      self.cola = aux_final.siguiente = Nodo(item)
      self.cola.anterior = aux_final
    self.tamanio += 1

  def agregar_al_inicio(self,item):
    if self.vacia():
      self.cabeza = self.cola = Nodo(item)
    else:
      aux_inicio = Nodo(item)
      aux_inicio.siguiente = self.cabeza
      self.cabeza.anterior = aux_inicio
      self.cabeza = aux_inicio

  def recorrer_lista(self):
    aux_inicio = self.cabeza
    while aux_inicio:
      print(aux_inicio.item)
      aux_inicio = aux_inicio.siguiente
  def insertar_interior(self,item,posicion=None)
    contador = 0
    aux = Nodo(item)
    if posicion == None:
      aux.anterior = self.cola
      self.cola.siguiente = aux
      self.cola = aux
    else:
      while contador <= posicion:
        contador += 1
        
