# import random
# import unittest
from TP1_LDE_testing.Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0 #almacena el número de nodos en la lista

    def __len__ (self):
        return self.tamanio

    def vacia(self):
        return self.cabeza is None

    def agregar(self, dato):#para probar que la lista se puede iterar correctamente
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
        copiar = ListaDobleEnlazada() #creamos una nueva instancia llamada "copiar" donde almacenamos la copia de la lista original
        aux = self.cabeza 
        while aux:
            copiar.agregar(aux.dato) #en cada iteración del bucle while se agrega el dato que se encuentra en aux a la lista copiar
            aux = aux.siguiente #una vez que se copia el dato anterior pasa al siguiente nodo
        return copiar #retorna la copia de la lista
    
    def agregar_al_inicio(self,item):
        if self.vacia():
            self.cabeza=self.cola=Nodo(item) #si la lista está vacía el nodo que se agrega va a ser el primer elemento y el último
        
        else: #si la lista no está vacía
            aux_inicio=Nodo(item) #aux_inicio contiene el nuevo dato que ingresará a la lista
            aux_inicio.siguiente=self.cabeza #se vuelven a establecer los enlaces del nodo que es la cabeza actual de la lista
            self.cabeza.anterior=aux_inicio 
            self.cabeza=aux_inicio #aux_inicio pasa a ser el primer nodo de la lista
        
        self.tamanio+=1
    def agregar_al_final(self,item):
        if self.vacia():
            self.cabeza=self.cola=Nodo(item)
        
        else:
            aux_final=self.cola #referencia al nodo que es la cola actualmente
            self.cola=aux_final.siguiente=Nodo(item) #Nodo(item) tiene el nuevo dato, siguiente del aux_final apunta al nuevo nodo conectando el nodo actual al nuevo nodo, se actualiza self.cola para que apunte al nuevo nodo
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

        elif (posicion == None) or (posicion == self.tamanio-1) or (posicion == -1):
            aux_actual = self.cola
            aux_eliminado = aux_actual.dato 
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
        return aux_eliminado #devuelte el elemento eliminado
    

    def ordenar(self):
        self._quick_sort(self.cabeza, self.cola) #llamamos al método quicksort de forma recursiva

    def _quick_sort(self, inicio, fin):#inicio y fin para definir el rango de la lista
        if inicio is not None and inicio != fin and inicio != fin.siguiente: #verifico si inicio no es igual a fin y si inicio no es igual al siguiente de fin
            pivote = self._particionar(inicio, fin) #llamo al método particionar para dividir el rango en 2, menores a la izq y mayores a la derecha del pivote
            if pivote:
                if pivote.anterior:
                    self._quick_sort(inicio, pivote.anterior) #se ordena la mitad desde inicio hasta el anterior al pivote
                if pivote.siguiente:
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
        concat_lista = self.copiar() #se crea una copia para evitar que se modifique la lista original
        if concat_lista.cola: #si la lista no está vacía
            concat_lista.cola.siguiente = nueva_lista.cabeza #el nodo que es la cola de concat_lista apuntará a la cabeza de nueva_lista
            if nueva_lista.cabeza is None: #verifico que "nueva_lista" no esté vacía
                nueva_lista.cabeza.anterior = concat_lista.cola #el nodo que actualmente es la cabeza de nueva_lista apuntará a la cola de concat_lista
            concat_lista.cola = nueva_lista.cola #la cola de concat_lista apunte a la cola de nueva_lista, para asegurarme de que la lista concatenada esté correctamente enlazada
        
        concat_lista.tamanio += nueva_lista.tamanio #tamaño total de la lista concatenada
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
