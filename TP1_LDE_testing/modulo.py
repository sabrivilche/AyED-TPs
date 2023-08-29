import random
import unittest
from Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

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
            yield aux.dato#muestra el nodo actual y avanza al siguiente
            aux = aux.siguiente

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


class Test_LDE(unittest.TestCase):
    """Test de la clase ListaDobleEnlazada"""

    def setUp(self):
        self.n_elementos = 200
        """ LDE vacía """
        self.lde_1 = ListaDobleEnlazada()

        """ LDE con elementos repetidos con lista auxiliar"""
        self.lde_2 = ListaDobleEnlazada()
        self.lista_aux_2 = random.choices(range(-self.n_elementos // 2, self.n_elementos // 2), k=self.n_elementos)
        for item in self.lista_aux_2:
            self.lde_2.agregar(item)

        """LDE de elementos no repetidos con lista auxiliar"""
        self.lde_3 = ListaDobleEnlazada()
        self.lista_aux_3 = random.sample(range(-self.n_elementos, self.n_elementos), self.n_elementos)
        for item in self.lista_aux_3:
            self.lde_3.agregar(item)

    def test_iteracion(self):
        nodo = self.lde_2.cabeza
        for dato in self.lde_2:
            self.assertEqual(nodo.dato, dato)
            nodo = nodo.siguiente
    
    def test_agregar_al_inicio(self):
            """
            pruebo que al agregar elementos al inicio de la lista
            la misma tiene tamaño correcto y se llena correctamente
            """
            valorNuevo = 25

            # Agregar al inicio de lista no vacia
            lde2_copia = self.lde_2.copiar()
            lde2_copia.agregar_al_inicio(valorNuevo)

            self.recorrer_lista(lde2_copia)
            self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                            "El tamaño de la lista luego de agregar debe incrementarse en uno")

            nodo_copia = lde2_copia.cabeza
            self.assertEqual(nodo_copia.dato, valorNuevo,
                            "El primer nodo no contiene el valor que se solicito agregar")

            nodo_copia = nodo_copia.siguiente
            nodo_original = self.lde_2.cabeza
            while nodo_original.siguiente is not None:
                self.assertEqual(nodo_original.dato, nodo_copia.dato,
                                "Se modificaron los datos de la lista luego de agregar el nuevo elemento")
                nodo_original = nodo_original.siguiente
                nodo_copia = nodo_copia.siguiente

            # Anexar en lista vacia (self.lde_1)
            lde1_copia = self.lde_1.copiar()
            lde1_copia.agregar_al_inicio(valorNuevo)

            self.recorrer_lista(lde1_copia)
            self.assertEqual(len(lde1_copia), 1,
                            "Al agregar un elemento al inicio de una lista vacia, su nuevo tamaño debe ser uno")

            self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                            "El nodo agregado a la lista vacia no contiene el valor que se solicito agregar")
            self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                        "En una lista de un elemento, la cabeza es la misma que la cola")

if __name__ == "__main__":
    unittest.main()

'''    def insertar_interior(self,item,posicion=None):
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
        
        elif posicion == None or posicion >= self.tamanio:#si no se agrega posición el nuevo elemento ingresa al final de la lista
              aux.anterior = self.cola
              self.cola.siguiente = aux
              self.cola = aux
              if posicion >= self.tamanio:
                  return Exception('Posición fuera de rango')#no se si esto está bien
        #lo de self.tamanio no debería mostrar un cartel que esa posición no existe en vez de agregarlo al final directamente? 
        else:
            actual = self.cabeza
            contador = 0

            while contador < posicion:
                actual = actual.siguiente
                contador += 1
            aux.siguiente = actual
            aux.anterior = actual.anterior
            aux.anterior.siguiente = aux#esto no era lo que habia dicho el profe que no existia?
            actual.anterior = aux
        self.tamanio += 1
'''
