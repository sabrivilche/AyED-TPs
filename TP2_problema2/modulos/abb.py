# -*- coding: utf-8 -*-
from datetime import datetime#Importo módulo datetime, para manipular fechas y horas

class NodoABB:
    def __init__(self, clave, valor):
        self.clave = clave #Clave del nodo, la uso para ordenar el árbol
        self.valor = valor #Valor asociado a la clave
        self.hijoIzquierdo = None #Punteros a los hijos izquierdo y derecho en el árbol
        self.hijoDerecho = None
        self.cargaUtil = valor

    def esHoja(self): #Verifica que el nodo sea una hoja, que no tenga hijos
        return self.hijoIzquierdo is None and self.hijoDerecho is None

    def tieneHijoIzquierdo(self): #Verifica si el nodo tiene un hijo izquierdo
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self): #Verifica si el nodo tiene un hijo derecho
        return self.hijoDerecho is not None
        

class ABB:
    def __init__(self):
        self.raiz = None #Nodo raiz inicialmente lo declaro como None
        self.tamano = 0 #Contador para saber el número de elementos del árbol

    def __len__(self):
        return self.tamano

    def agregar(self, clave, valor): #Agrego clave-valor al árbol
        self.raiz = self._agregar(self.raiz, clave, valor)
        self.tamano += 1 #Incremento el tamaño del árbol después de agregar los elementos

    def _agregar(self, nodo, clave, valor): #Método auxiliar para realizar la inserción de un nodo al árbol
        if nodo is None:
            return NodoABB(clave, valor) #Si el nodo actual es None creo un nuevo nodo

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._agregar(nodo.hijoIzquierdo, clave, valor)
        
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._agregar(nodo.hijoDerecho, clave, valor)
        
        else:
            nodo.valor = valor #Si la clave ya existe actualizo el valor

        return nodo


    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)
        self.tamano -= 1
    
    def _encontrar_sucesor(self, nodo):# Encuentra el sucesor de un nodo dado (el nodo más pequeño en su subárbol derecho).
        
        if nodo is None:
            return None

        actual = nodo
        
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo

        return actual
    
    def _eliminar(self, nodo, clave):
        if nodo is None:
            raise KeyError(f"Clave '{clave}' no encontrada en el árbol")  # Lanzar excepción si la clave no existe

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._eliminar(nodo.hijoIzquierdo, clave)
        
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, clave)
        
        else:
            # Caso 1: Nodo con un hijo o sin hijos
            if nodo.hijoIzquierdo is None:
                return nodo.hijoDerecho
            elif nodo.hijoDerecho is None:
                return nodo.hijoIzquierdo

            # Caso 2: Nodo con dos hijos
            sucesor = self._encontrar_sucesor(nodo.hijoDerecho)
            nodo.clave = sucesor.clave
            nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, sucesor.clave)

        return nodo

    def obtener(self, clave):
        return self._obtener(self.raiz, clave)

    def _obtener(self, nodo, clave):
        if nodo is None:
            raise KeyError(f"Clave '{clave}' no encontrada en el árbol")

        if clave == nodo.clave:
            return nodo.valor
        
        elif clave < nodo.clave:
            return self._obtener(nodo.hijoIzquierdo, clave)
        
        else:
            return self._obtener(nodo.hijoDerecho, clave)

    def __contains__(self, clave):
        try:
            self._obtener(self.raiz, clave) #Busqueda de la clave
            return True
        
        except KeyError: #Si la clave no se encuentra en el árbol
            return False

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __delitem__(self, clave):
        self.eliminar(clave)

    def __iter__(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo): #Nodo es la raíz del subárbol que se recorre
        if nodo is not None:
            yield from self._inorden(nodo.hijoIzquierdo) #Llamada recursiva al método _inorden en el hijo izq del nodo actual
            #Primero recorro todos los nodos del subárbol izq
            yield (nodo.clave, nodo.valor) #Genera una tupla que contenga la clave y valor del nodo actual, esta tupla se devuelve para cada nodo recorrido
            yield from self._inorden(nodo.hijoDerecho) #Llamada recursiva pero en el hijo derecho del nodo actual

    def guardar_temperatura(self, temperatura, fecha):
        self.agregar(clave=fecha, valor=temperatura)

    def devolver_temperatura(self, fecha):
        return self.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2): #Encuentra la temp máxima dentro de un rango de fechas
        max_temp = float("-inf") #Inicializo la variable con un valor negativo infinito para que cualquier temperatura que se encuentre dentro del rango sea mayor que max_temp
        
        for self.fecha, temp in self._in_rango(fecha1, fecha2): #_in_rango proporciona pares de fechas y temperaturas dentro del rango dado
            max_temp = max(max_temp, temp)
        
        return max_temp

    def min_temp_rango(self, fecha1, fecha2):
        min_temp = float("inf")
        
        for self.fecha, temp in self._in_rango(fecha1, fecha2):
            min_temp = min(min_temp, temp)
        
        return min_temp

    def temp_extremos_rango(self, fecha1, fecha2):
        min_temp = float("inf")
        max_temp = float("-inf")
        
        for self.fecha, temp in self._in_rango(fecha1, fecha2): #tupla self.fecha, temp representa la fecha y la temperatura asociada a un nodo dentro del rango de fechas
            min_temp = min(min_temp, temp)
            max_temp = max(max_temp, temp)
        
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        self.eliminar(fecha)

    def devolver_temperaturas(self, fecha1, fecha2):
        temp_list = []
        
        for fecha, temp in self._in_rango(fecha1, fecha2):
            temp_list.append(f"{fecha}: {temp} ºC")
        
        return temp_list

    def cantidad_muestras(self):
        return self.tamano

    def _in_rango(self, fecha1, fecha2):
        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1
        
        return self._in_rango_rec(self.raiz, fecha1, fecha2)

    def _in_rango_rec(self, nodo, fecha1, fecha2):
        if nodo is not None:
            if fecha1 <= nodo.clave <= fecha2: #Verifico que el nodo actual esté dentro del rango de fechas
                yield nodo.clave, nodo.valor #Genero un par clave-valor que contenga la fecha y el valor del nodo actual
            if fecha1 < nodo.clave: #Si fecha1 es menor que la clave se verifica si hay nodos dentro del subárbol izquierdo que estén dentro del rango de fechas
                yield from self._in_rango_rec(nodo.hijoIzquierdo, fecha1, fecha2) 
            if fecha2 > nodo.clave:
                yield from self._in_rango_rec(nodo.hijoDerecho, fecha1, fecha2)
