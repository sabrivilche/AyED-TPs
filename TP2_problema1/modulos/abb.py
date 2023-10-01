# -*- coding: utf-8 -*-
from datetime import datetime#Importo módulo datetime, para manipular fechas y horas


class NodoABB:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

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
            nodo.izquierda = self._agregar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._agregar(nodo.derecha, clave, valor)

        return nodo

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return nodo

        if clave < nodo.clave:
            nodo.izquierda = self._eliminar(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._eliminar(nodo.derecha, clave)
        else:
            # Caso 1: Nodo con un hijo o sin hijos
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 2: Nodo con dos hijos
            sucesor = self._encontrar_sucesor(nodo.derecha)
            nodo.clave = sucesor.clave
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.clave)

        return nodo

    def obtener(self, clave):
        return self._obtener(self.raiz, clave)

    def _obtener(self, nodo, clave):
        if nodo is None:
            raise KeyError(f"Clave '{clave}' no encontrada en el árbol")

        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._obtener(nodo.izquierda, clave)
        else:
            return self._obtener(nodo.derecha, clave)

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
            yield from self._inorden(nodo.izquierda)
            yield (nodo.clave, nodo.valor)
            yield from self._inorden(nodo.derecha)

