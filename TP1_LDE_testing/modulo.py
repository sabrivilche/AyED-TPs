import random
import unittest
from TP1_LDE_testing.Nodo import Nodo

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
    
    # def ordenar(self): 
    #     copia_lista = list(self) #hago una copia de la lista, cambio la lista enlazada a una de `python` para poder ordenarla más fácil usando las funciones de python
                
    #     copia_lista = sorted(copia_lista) #ordeno la lista con sorted para mejorar el tiempo (orden n)
        
    #     aux_ordenar = self.cabeza #me posiciono en la cabeza para empezar a recorrer la lista e ir actualizandola de forma ordenada
    #     for item in copia_lista:
    #         aux_ordenar.dato = item #posicionado en aux le asigna el elemento ordenado a dato 
    #         aux_ordenar = aux_ordenar.siguiente #me muevo al siguiente nodo

    # def ordenar(self): #ordenamiento por inserción
    #     if self.vacia() or self.tamanio <= 1:
    #         return

    #     nodo_actual = self.cabeza.siguiente #empiezo a recorrer la lista a partir del segundo elemento

    #     while nodo_actual is not None:
    #         dato_actual = nodo_actual.dato #elemento del nodo actual lo asignamos a dato_actual
    #         nodo_anterior = nodo_actual.anterior #nodo anterior al actual y lo asignamos a nodo_actual

    #         while nodo_anterior is not None and nodo_anterior.dato > dato_actual: #nodo_anterior sea mayor que dato_actual, voy corriendo los datos mayores al principio de la lista
    #             nodo_actual.dato = nodo_anterior.dato #el elemento de nodo_anterior pasa a estar en nodo_actual, para desplazar el actual hacia "atrás"
    #             nodo_actual = nodo_anterior #actualizo el nodo
    #             nodo_anterior = nodo_actual.anterior #nodo_anterior pasa a ser el anterior al nodo_actual

    #         nodo_actual.dato = dato_actual #una vez que se ordenan los elementos asignamos el elemento guardado en dato_actual a nodo_actual
    #         nodo_actual = nodo_actual.siguiente #pasamos al siguiente nodo para seguir ordenando

    def ordenar(self):
        self._quick_sort(self.cabeza, self.cola) #llamamos al método quicksort de forma recursiva

    def _quick_sort(self, inicio, fin):#inicio y fin para definir el rango de la lista
        if inicio is not None and inicio != fin and inicio != fin.siguiente: #verifico si inicio no es igual a fin y si inicio no es igual al siguiente de fin
            pivote = self._particionar(inicio, fin) #llamo al método particionar para dividir el rango en 2, menores a la izq y mayores a la derecha del pivote
            self._quick_sort(inicio, pivote.anterior) #se ordena la mitad desde inicio hasta el anterior al pivote
            self._quick_sort(pivote.siguiente, fin) #se ordena la mitad desde el siguiente del pivote hasta fin

    def _particionar(self, inicio, fin):
        pivote = fin #nodo final del rango actual de la lista
        nodo_rango = inicio #primer nodo del rango

        while nodo_rango != pivote: #mientas inicio y fin no sean iguales
            if nodo_rango.dato <= pivote.dato: #comparo el elemento de nodo_rango para ver si es menor o igual al elemento en pivote
                nodo_rango.dato, inicio.dato = inicio.dato, nodo_rango.dato #si se cumple la condición anterior se intercambian los elementos de los nodos
                inicio = inicio.siguiente #pasamos al siguiente nodo
            nodo_rango = nodo_rango.siguiente #el puntero se mueve al siguiente nodo de la lista

        inicio.dato, pivote.dato = pivote.dato, inicio.dato #una vez que se recorrió toda la lista intercambiamos los elementos
        #el elemento dentro del nodo inicio pasa a ser el primer valor mayor al pivote
        return inicio


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