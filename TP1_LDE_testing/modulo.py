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
            
    def recorrer_lista(self, lista):
        #Adelante para atras
        aux_nodo = lista.cabeza #nos posicionamos en el primer elemento de la lista
        contador = 0 #contador para los nodos
        aux_lista = [] #lista vacia para almacenar los datos mientras se recorre la lista

        assert aux_nodo.anterior is None #Elemento anterior a la cabeza tiene que ser None, si no es así va a mostrar un mensaje

        while aux_nodo is not None:#recorre la lista de principio a fin
            contador += 1 #se incrementa el contador en cada iteración
            aux_lista.append(aux_nodo.dato) #se van agregando los nodos recorridos a la lista aux_lista
            aux_nodo = aux_nodo.siguiente #pasamos al siguiente nodo

        assert len(lista) == contador #El valor de contador debe coincidir con el tamaño de la lista, de lo contrario muestra un mensaje

        #Atrás para adelante
        aux_nodo = lista.cola #nos posicionamos en el último elemento

        assert aux_nodo.siguiente is None #El nodo siguiente al nodo cola tiene que ser None

        while aux_nodo is not None: #los elementos deben ser los mismos que en el recorrido de adelante para atrás
            contador -= 1
            assert aux_lista[contador] == aux_nodo.dato #si los nodos no son los mismos mostrará un mensaje
            aux_nodo = aux_nodo.anterior #pasamos al nodo anterior

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

    def insertar_interior(self,item,posicion = None):
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


    def extraer_interior(self, posicion = None):
        if self.vacia():
            raise Exception('La lista está vacía')

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception('Posición fuera de rango')

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
    
    def recorrer_lista(self, lista):
        """
        Metodo auxiliar para usar en tests de métodos complejos
        de la clase lista doblemente enlazada. Verifica que los nodos de la lista
        esten bien enlazados entre sí (forward y backward).
        """

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
    def test_agregar_al_final(self):
        """
        pruebo que al anexar elementos al final de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """

        valorNuevo = 25

        # Anexar en lista no vacia
        lde2_copia = self.lde_2.copiar()
        lde2_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde2_copia)
        self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                         "El tamaño de la lista luego de anexar debe incrementarse en uno")

        nodo_original = self.lde_2.cabeza
        nodo_copia = lde2_copia.cabeza
        while nodo_original.siguiente is not None:
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Se modificaron los datos de la lista luego de anexar el nuevo elemento")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

        nodo_copia = nodo_copia.siguiente
        self.assertEqual(nodo_copia.dato, valorNuevo,
                         "El ultimo nodo no contiene el valor que se solicito agregar")
        self.assertIs(nodo_copia, lde2_copia.cola,
                      "El ultimo nodo no coincide con la refencia a la cola de la lista")

        # Anexar en lista vacia (self.lde_1)
        lde1_copia = self.lde_1.copiar()
        lde1_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde1_copia)
        self.assertEqual(len(lde1_copia), 1,
                         "Al anexar un elemento en una lista vacia, su nuevo tamaño debe ser uno")

        self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                         "El nodo anexado a la lista vacia no contiene el valor que se solicito agregar")
        self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                      "En una lista de un elemento, la cabeza es la misma que la cola")
        
    def test_insertar_interior(self):
        """
        pruebo insertar un ítem en una posición aleatoria
        de la LDE y compruebo que el elemento es insertado
        """
        # print(f"\nPosición aleatoria donde se inserta: {self.posicion}")
        posicion = random.randint(1, self.n_elementos - 1)

        self.lde_2.insertar_interior(250, posicion)
        self.n_elementos += 1
        self.assertEqual(self.lde_2.tamanio, self.n_elementos)

        contador = 0
        nodo_actual = self.lde_2.cabeza
        valor = None
        while nodo_actual and contador != posicion:
            contador += 1
            nodo_actual = nodo_actual.siguiente
            valor = nodo_actual.dato

        self.assertEqual(valor, 250)

    def test_insertar_extremos(self):
        """
        inserto ítems en los extremos de la LDE, compruebo
        tamaño correcto y su valor.
        """

        """inserto 1er item al inicio"""
        self.lde_2.insertar_interior(120, 0)
        self.n_elementos += 1
        self.assertEqual(len(self.lde_2), self.n_elementos)
        self.assertEqual(self.lde_2.cabeza.dato, 120)

        """inserto 2do item en la última posición"""
        self.lde_2.insertar_interior(180, len(self.lde_2) - 1)
        self.n_elementos += 1
        self.assertEqual(len(self.lde_2), self.n_elementos)
        nodo_actual = self.lde_2.cabeza
        nodo_anterior = None
        valor = None
        while nodo_actual.siguiente:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            valor = nodo_anterior.dato
        self.assertEqual(valor, 180)

    def test_excepciones_insertar(self):
        """
        intento insertar en posiciones incorrectas o no existentes de
        la LDE y compruebo que se lanzan las excepciones correspondientes
        """
        self.assertRaises(Exception, self.lde_2.insertar_interior, 210, -10,
                          "La LDE debe arrojar excepcion al intentar insertar en posición negativa")
        self.assertRaises(Exception, self.lde_2.insertar_interior, 210, self.n_elementos + 10,
                          "La LDE debe arrojar excepcion al intentar insertar en posición mayor al tamaño")
    
    def test_operador_len(self):
        """
        Prueba que este sobrecargado el operador len() para la LDE
        """
        self.assertEqual(len(self.lde_1), 0, "No funciona el operador len() en la LDE")
        self.assertEqual(len(self.lde_2), self.n_elementos, "No funciona el operador len() en la LDE")

    def test_extraer_interior(self):
        """
        extraigo un elemento de una posición aleatoria de la lista
        con elementos no repetidos y compruebo que el mismo no permanece
        en la lista
        """
        posicion = random.randint(1, self.n_elementos - 1)
        lde3_copia = self.lde_3.copiar()

        item = lde3_copia.extraer_interior(posicion)

        # Verifico tamaño
        self.assertEqual(len(lde3_copia), len(self.lde_3) - 1,
                         "No se modifico correctamente el tamaño de la lista luego de la extracción")

        # Verifico que este correctamente enlazada
        self.recorrer_lista(lde3_copia)

        nodo_original = self.lde_3.cabeza
        nodo_copia = lde3_copia.cabeza
        contador_pos = 0
        while nodo_original is not None:
            if contador_pos == posicion:
                self.assertEqual(nodo_original.dato, item,
                                 "El elemento extraido no coincide con el elemento originariamente en la posicion solicitada")
                nodo_original = nodo_original.siguiente
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Luego de la extracción los demás elementos de la lista se vieron alterados")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente
            contador_pos += 1
    def test_excepciones_extraer(self):
        """
        pruebo extraer en una lista vacía y en posiciones fuera
        de los límites de la LDE. Compruebo las excepciones
        """
        # LDE vacía
        self.assertRaises(Exception, self.lde_1.extraer_interior,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer_interior, 0,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer_interior, -1,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer_interior, self.n_elementos - 1,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer_interior, self.n_elementos + 10,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer_interior, -(self.n_elementos + 10),
                          "Extraer de una lista vacia deberia arrojar un error")

        # LDE no vacia
        self.assertRaises(Exception, self.lde_2.extraer_interior, -50,
                          "Extraer de una posicion negativa dede arrojar error")
        self.assertRaises(Exception, self.lde_2.extraer_interior, self.n_elementos + 50,
                          "Extraer de una posicion mayor al tamaño de la lista menos uno dede arrojar error")
       
    
'''    def test_extraer_extremos(self):
        """
        pruebo extraer ítems al inicio y al final de la LDE
        con/sin parámetro, verifico el valor extraído y el tamaño
        resultante de la LDE
        """
        # Extraer al inicio
        self.assertEqual(self.lde_3.extraer_interior(0), self.lista_aux_3.pop(0),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(len(self.lde_3), self.n_elementos - 1,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final sin parámetro
        self.assertEqual(self.lde_3.extraer_interior(), self.lista_aux_3.pop(),
                         "Cuando no se pasa argumento, se debe extraer el ultimo elemento de la lista")
        self.assertEqual(len(self.lde_3), self.n_elementos - 2,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final usando parámetro
        self.assertEqual(self.lde_3.extraer_interior(len(self.lde_3) - 1), self.lista_aux_3.pop(),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(self.lde_3.tamanio, self.n_elementos - 3,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final parámetro -1
        self.assertEqual(self.lde_3.extraer_interior(-1), self.lista_aux_3.pop(),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(self.lde_3.tamanio, self.n_elementos - 4,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)
    
'''
if __name__ == "__main__":
    unittest.main()
    
