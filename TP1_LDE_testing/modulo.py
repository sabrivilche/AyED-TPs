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
            
    #def recorrer_lista(self,lista):
     #   aux = lista.cabeza
      #  aux_tamanio = 0 #el tamaño actual de la lista
       # anterior = None
        #while aux:
         #   aux_tamanio += 1
          #  if anterior:
           #     self.assertIs (anterior.siguiente, aux, "Enlace nterior no es igual a enlace actual")
            #    anterior = aux
             #   aux = aux.siguiente
        #self.assertEqual (aux_tamanio, len(lista),"Tamaño de lista diferente a los nodos recorridos")

    def recorrer_lista(self, lista):
        
        # Recorro de adelante para atras
        nodo = lista.cabeza
        counter = 0
        elementos = []

        self.assertIsNone(nodo.anterior,
                          "El elemento anterior a la cabeza de la lista debe ser None")

        while nodo is not None:
            counter += 1
            elementos.append(nodo.dato)
            nodo = nodo.siguiente

        self.assertEqual(len(lista), counter,
                         "Tamaño informado por la lista no coincide con la cantidad de nodos en la misma.")

        # Recorro de atras para adelante
        nodo = lista.cola

        self.assertIsNone(nodo.siguiente,
                          "El elemento siguiente a la cola de la lista debe ser None")

        while nodo is not None:
            counter -= 1
            self.assertEqual(elementos[counter], nodo.dato,
                             "Los elementos en la lista recorrida de atras para adelante son diferentes "
                             "a que si la recorremos de adelante para atrás.")
            nodo = nodo.anterior

    def copiar(self):
        copiar = ListaDobleEnlazada()
        aux = self.cabeza
        while aux:
            copiar.agregar(aux.dato)
            aux = aux.siguiente
        return copiar




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

        # self.posicion = random.randint(1, self.n_elementos - 1)  # randint incluye el extremo

    def test_iteracion(self):

        nodo = self.lde_2.cabeza
        for dato in self.lde_2:
            self.assertEqual(nodo.dato, dato,
                                "Los datos arrojados en el for no coinciden con los datos "
                                "obtenidos por recorrido manual de la LDE desde la cabeza")
            nodo = nodo.siguiente
    

    def test_copiar(self):
        """
        hago una copia de una LDE con elementos y sin elementos
        y comparo nodo a nodo para verificar la copia.
        """
        lde_3_copia = self.lde_3.copiar()

        # Compruebo la integridad fisica de la lista original
        self.recorrer_lista(self.lde_3)
        # Compruebo que la lista copiada este correctamente enlazada
        self.recorrer_lista(lde_3_copia)

        nodo_original = self.lde_3.cabeza
        nodo_copia = lde_3_copia.cabeza

        # Compruebo longitud de las listas
        self.assertEqual(len(lde_3_copia), len(self.lde_3),
                         "Los tamaños de las listas copiadas nos son las mismas.")
        # Compruebo que las listas sean instancias diferentes
        self.assertIsNot(lde_3_copia, self.lde_3,
                         "Las listas copiadas son referencias al mismo espacio de memoria.")

        while nodo_original or nodo_copia:
            # Compruebo igualdad del contenido de ambas listas
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Los datos de la lista copiada no son iguales a los de la lista original")
            # Compruebo que los nodos de ambas listas sean instancias diferentes
            self.assertIsNot(nodo_original, nodo_copia,
                             "Los nodos de las lista copiada son compartidos con los de la lista original")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente
'''    
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
                      "En una lista de un elemento, la cabeza es la misma que la cola")'''

if __name__ == "__main__":
    unittest.main()
    
''' def agregar_al_inicio(self,item):
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


    def insertar_interior(self,item,posicion=None):
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