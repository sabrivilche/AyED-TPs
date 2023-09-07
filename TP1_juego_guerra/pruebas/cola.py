import random

class Cola:
    def __init__(self):
        self.mazo = []

        self.tamanio = 0


    def vacia(self):

        return len(self.mazo) == 0
    

    def agregar_carta(self,dato):#se agrega una sola carta(dato) a la cola
        self.mazo.append(dato)

        self.tamanio += 1
    

    def agregar_cartas(self,dato): #se agrega una lista de cartas al final de la cola self.carta
        self.mazo.extend(dato)

    def sacar_carta(self):

        return self.mazo.pop(0)
    
    def tamanio(self):

        return len(self.mazo)
    
    def mezclar_mazo(self):

        random.shuffle(self.mazo)


