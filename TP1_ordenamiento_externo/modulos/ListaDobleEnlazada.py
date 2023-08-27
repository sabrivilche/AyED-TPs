from Nodo import Nodos

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

    def agregar_al_inicio(self,item):
        if self.vacia():
            self.cabeza = self.cola=Nodos(item)

        else:
            aux=Nodos(item)
            aux.siguiente=self.cabeza
            self.cabeza.anterior = aux
            self.cabeza=aux
        
        tamanio+=1

    def agregar_al_final(self,item):
        if self.vacia():
            self.cabeza=self.cola=Nodos(item)
        
        else:
            aux=self.cola
            self.cola=aux.siguiente=Nodos(item)
            self.cola.anterior=aux

        tamanio+=1

    #def insertar_interior(self,item,posicion=None):


        


     