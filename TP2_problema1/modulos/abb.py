# -*- coding: utf-8 -*-
from datetime import datetime#Importo módulo datetime, para manipular fechas y horas


class NodoABB:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.cargaUtil = valor
        
    def esHoja(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None
        

class ABB:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        self.raiz = self._agregar(self.raiz, clave, valor)

    def _agregar(self, nodo, clave, valor):
        if nodo is None:
            return NodoABB(clave, valor)

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._agregar(nodo.hijoIzquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._agregar(nodo.hijoDerecho, clave, valor)
        else:
            nodo.valor = valor

        return nodo


    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return nodo

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
            self._obtener(self.raiz, clave)
            return True
        except KeyError:
            return False

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __delitem__(self, clave):
        self.eliminar(clave)

    def __iter__(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            yield from self._inorden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.valor)
            yield from self._inorden(nodo.hijoDerecho)

    def guardar_temperatura(self, temperatura, fecha):
        self.agregar(clave=fecha, valor=temperatura)

    def devolver_temperatura(self, fecha):
        return self.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        max_temp = float("-inf")
        for fecha, temp in self._in_rango(fecha1, fecha2):
            max_temp = max(max_temp, temp)
        return max_temp

    def min_temp_rango(self, fecha1, fecha2):
        min_temp = float("inf")
        for fecha, temp in self._in_rango(fecha1, fecha2):
            min_temp = min(min_temp, temp)
        return min_temp

    def temp_extremos_rango(self, fecha1, fecha2):
        min_temp = float("inf")
        max_temp = float("-inf")
        for fecha, temp in self._in_rango(fecha1, fecha2):
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
            if fecha1 <= nodo.clave <= fecha2:
                yield nodo.clave, nodo.valor
            if fecha1 < nodo.clave:
                yield from self._in_rango_rec(nodo.hijoIzquierdo, fecha1, fecha2)
            if fecha2 > nodo.clave:
                yield from self._in_rango_rec(nodo.hijoDerecho, fecha1, fecha2)
