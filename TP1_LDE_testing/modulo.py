from Nodo import Nodo


class ListaDobleEnlazada:

    def __init__(self):

        self.cabeza=None

        self.cola=None

        self.tamanio=0


    def vacia(self):

        return self.cabeza==None


    def recorrer_lista(self):

        aux_inicio = self.cabeza

        while aux_inicio:

          print(aux_inicio.dato)

          aux_inicio = aux_inicio.siguiente


    def agregar_al_inicio(self,item):

        if self.vacia():

            self.cabeza = self.cola=Nodo(item)

        else:

            aux=Nodo(item)

            aux.siguiente=self.cabeza

            self.cabeza.anterior = aux

            self.cabeza=aux
        

        self.tamanio += 1


    def agregar_al_final(self,item):

        if self.vacia():

            self.cabeza=self.cola=Nodo(item)
        
        else:
            aux=self.cola

            self.cola=aux.siguiente=Nodo(item)
            self.cola.anterior=aux


        self.tamanio += 1


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


        


     