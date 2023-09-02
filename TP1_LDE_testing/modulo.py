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
                self.tamanio -= 1 #reduce el tamaño de la lista
        elif (posicion == None) or (posicion == self.tamanio-1):
                aux_actual = self.cola
                aux_eliminado = aux_actual.dato 
                #aux_actual.anterior = self.cola
                aux_actual.anterior.siguiente = None
                self.cola = aux_actual.anterior
                self.tamanio -= 1 #reduce el tamaño de la lista
        return aux_eliminado #devuelte el elemento eliminado
    
    def ordenar(self):
        copia_lista = list(self) #hago una copia de la lista, cambio la lista enlazada a una de `python` para poder ordenarla más fácil usando las funciones de python
                
        copia_lista = sorted(copia_lista) #ordeno la lista con sorted para mejorar el tiempo (orden n)
        
        aux_ordenar = self.cabeza #me posiciono en la cabeza para empezar a recorrer la lista e ir actualizandola de forma ordenada
        for item in copia_lista:
            aux_ordenar.dato = item #posicionado en aux le asigna el elemento ordenado a dato 
            aux_ordenar = aux_ordenar.siguiente #me muevo al siguiente nodo


    def __add__(self,nueva_lista):
        concat_lista = self.copiar()
        if concat_lista.cola:
            concat_lista.cola.siguiente = nueva_lista.cabeza
            if nueva_lista.cabeza is None:
                nueva_lista.cabeza.anterior = concat_lista.cola
            concat_lista.cola = nueva_lista.cola
        
        concat_lista.tamanio += nueva_lista.tamanio
        return concat_lista

    def concatenar(self,nuevalista):
        nuevalista_copia = nuevalista.copiar()

        if self.cola is None: #si la lista está vacía se copia la cabeza y cola en la nuevalista_copia
            self.cabeza = nuevalista_copia.cabeza
            self.cola = nuevalista_copia.cola
        else: 
            self.cola.siguiente = nuevalista_copia.cabeza #apunto al siguiente nodo de la cola y le asigno la cabeza de la otra lista
            nuevalista_copia.cabeza.anterior = self.cola #al nodo anterior a la cabeza de la nuevalista_copia se le asigna la cola
            self.cola = nuevalista_copia.cola #nuevalista_copia va a apuntar al último nodo de la nueva lista
        self.tamanio += nuevalista.tamanio

    def invertir(self):
        if self.vacia() or self.cabeza == self.cola: #si la lista está vacia o tiene un solo elemento
            return
        
        nodo_actual = self.cabeza #me posiciono en la cabeza para ir recorriendo la lista original

        while nodo_actual is not None:
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior,nodo_actual.siguiente #intercambio los nodos
            nodo_actual = nodo_actual.anterior #para avanzar en la lista le asigno al nodo_actual el nodo anterior, para poder moverme hacia atrás

        self.cabeza,self.cola = self.cola, self.cabeza #para asegurarme de que se invierta la lista


    