import random
import unittest
from Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __len__ (self):
        return self.tamanio

    def vacia(self):
        return self.cabeza is None

    def agregar(self, dato):#para probar que la lista te puede iterar correctamente
        aux = Nodo(dato)
        if self.vacia():
            self.cabeza = aux
            self.cola = aux
        else:
            aux.anterior = self.cola
            self.cola.siguiente = aux
            self.cola = aux
        self.tamanio += 1

    def __iter__(self):
        aux = self.cabeza
        while aux:
            yield aux.dato
            aux = aux.siguiente
            

    def copiar(self):
        copiar = ListaDobleEnlazada()
        aux = self.cabeza
        while aux:
            copiar.agregar(aux.dato)
            aux = aux.siguiente
        return copiar
    
    def agregar_al_inicio(self,item):
        if self.vacia():
            self.cabeza=self.cola=Nodo(item)
        
        else:
            aux_inicio=Nodo(item)
            aux_inicio.siguiente=self.cabeza
            self.cabeza.anterior=aux_inicio
            self.cabeza=aux_inicio
        
        self.tamanio+=1
    def agregar_al_final(self,item):
        if self.vacia():
            self.cabeza=self.cola=Nodo(item)
        
        else:
            aux_final=self.cola
            self.cola=aux_final.siguiente=Nodo(item)
            self.cola.anterior=aux_final
        
        self.tamanio+=1

    def insertar(self,item,posicion = None):
        aux = Nodo(item)
        if self.vacia():#si la lista está vacia el item ingresado es la cabeza y cola a la vez
            self.cabeza = aux
            self.cola = aux
            self.tamanio += 1
            return
        
        if posicion == 0:#si la posición dada es = 0 la cabeza pasa a ser el dato siguiente y el aux la cabeza
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        
        elif posicion == None:#si no se agrega posición el nuevo elemento ingresa al final de la lista
              aux.anterior = self.cola
              self.cola.siguiente = aux
              self.cola = aux
              if posicion >= self.tamanio:
                  return Exception('Posición fuera de rango')#Si la posición ingresada es mayor que el tamaño de la lista muestra un mensaje
              
        else:
            actual = self.cabeza
            contador = 0

            while contador < posicion:
                actual = actual.siguiente
                contador += 1
            aux.siguiente = actual
            aux.anterior = actual.anterior
            aux.anterior.siguiente = aux
            actual.anterior = aux
        self.tamanio += 1


    def extraer(self, posicion=None):
        if self.vacia():
            raise Exception('La lista está vacía')

        elif (posicion == None) or (posicion == self.tamanio-1) or (posicion == -1):#agregamos posición == -1
            aux_actual = self.cola
            aux_eliminado = aux_actual.dato 
            #aux_actual.anterior = self.cola
            aux_actual.anterior.siguiente = None
            self.cola = aux_actual.anterior
            self.tamanio -= 1 #reduce el tamaño de la lista

        elif (posicion is not None) and (posicion != self.tamanio -1):
            if  posicion < 0 or posicion >= self.tamanio:
                raise Exception('Posición fuera de rango')
            else: 
                aux_actual = self.cabeza #primer nodo

                for _ in range(posicion):#me muevo "posicion" veces, en cada iteración se actualiza "aux_actual"
                    aux_actual = aux_actual.siguiente

                aux_eliminado = aux_actual.dato #guardo el dato eliminado en "aux_eliminado"
                anterior = aux_actual.anterior #nodos anterior y siguiente al nodo aux_actual
                siguiente = aux_actual.siguiente
                if anterior: #si anterior no es None
                    anterior.siguiente = siguiente #el enlace del nodo siguiente al nodo anterior se actualiza para "saltar" el nodo eliminado (aux_eliminar)
                else: #si es None
                    self.cabeza = siguiente #la cabeza será el nodo siguiente

                if siguiente: #si siguiente no es None
                    siguiente.anterior = anterior #el enlace del nodo anterior al nodo siguiente se actualiza para "saltar" el nodo eliminado (aux_eliminar)
                else: #si es None
                    self.cola = anterior #la cola pasa a ser el nodo anterior
                self.tamanio -= 1

        elif (posicion == None) or (posicion == self.tamanio-1):
            aux_actual = self.cola
            aux_eliminado = aux_actual.dato 
            #aux_actual.anterior = self.cola
            aux_actual.anterior.siguiente = None
            self.cola = aux_actual.anterior
            self.tamanio -= 1 

        #reduce el tamaño de la lista
        return aux_eliminado #devuelte el elemento eliminado
    

    def particion(ultimo,primero):
        pivote=ultimo.dato
        i=ultimo.anterior
        for j in range(ultimo,primero):
            if j.dato<=pivote:
                i=ultimo if not i else i.siguiente
                i.dato,j.dato=j.dato,i.dato
            i=ultimo if not i else i .siguiente
            i.dato,primero.dato=primero.dato,i.dato
            return i
        
    def ordenamientoAux(ultimo,primero):
        if primero and ultimo!=primero and ultimo!=primero.siguiente:
            aux=particion(ultimo,primero)#aparece que no está definido particion
            ordenamientoAux(ultimo,aux.anterior)
            ordenamientoAux(aux.siguiente,primero)

    def ordenar(self):
        
        self.ordenamientoAux(primero=self.cabeza)#No se que está pasanda

'''def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.prev = None
    new_node.next = head_ref
    if head_ref:
        head_ref.prev = new_node
    head_ref = new_node
    return head_ref

    La función push se utiliza para insertar un nuevo elemento al principio de la lista doblemente enlazada.
    #def printList(self, node):
     #   while node is not None:
      #      print(node.data, end=" ")
       #     node = node.next


    def quickSort(self, left, right):
        if right is not None and left != right and left != right.next:
            p = self.partition(left, right)
            self.quickSort(left, p.prev)
            self.quickSort(p.next, right)

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
Imprime los elementos de la lista
'''