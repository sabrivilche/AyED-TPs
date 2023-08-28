from Nodo import Nodo


class ListaDobleEnlazada:


    def __init__(self):

        self.cabeza=None

        self.cola=None

        self.tamanio=0


    def vacia(self):

        return self.cabeza==None


    def recorrer_lista(self):

        aux=self.cabeza

        while aux:

            print(aux.dato)#No reconoce variable item

            aux=aux.siguiente

    def agregar(self, item):
        aux = Nodo(item)
        if not self.cabeza:
            self.cabeza = aux
            self.cola = aux
        else:
            aux.anterior = self.cola
            self.cola.siguiente = aux
            self.cola = aux

    def agregar_al_inicio(self,item):

        if self.vacia():

            self.cabeza = self.cola=Nodo(item)

        else:

            aux=Nodo(item)

            aux.siguiente=self.cabeza

            self.cabeza.anterior = aux

            self.cabeza=aux
        

        self.tamanio+=1


    def agregar_al_final(self,item):

        if self.vacia():

            self.cabeza=self.cola=Nodo(item)
        
        else:
            aux=self.cola

            self.cola=aux.siguiente=Nodo(item)
            self.cola.anterior=aux


        self.tamanio+=1


    def __iter__(self):

        aux_inicio = self.cabeza

        while aux_inicio:

          print(aux_inicio.item)

          aux_inicio = aux_inicio.siguiente


    def insertar_interior(self,item,posicion=None):

        contador = 0

        aux = Nodo(item)

        if posicion == None:
              aux.anterior = self.cola

              self.cola.siguiente = aux
              self.cola = aux

        elif posicion > 0 and posicion <= self.tamanio:
            self.anterior = aux

            aux.siguiente = aux

        #else:

         #     while contador <= posicion:

          #      contador += 1

        


     

