import random
class Cola:
    def __init__(self):
        self.carta = []
        self.tamanio = 0

    def vacia(self):
        return len(self.carta) == 0
    
    def agregar_carta(self,dato):#se agrega una sola carta(dato) a la cola
        self.carta.append(dato)
        self.tamanio += 1
    
    def agregar_cartas(self,dato): #se agrega una lista de cartas al final de la cola self.carta
        self.carta.extend(dato)

    def sacar_carta(self):
<<<<<<< HEAD
        self.lanzar_carta = self.carta.pop(0)
=======
        self.lanzar_carta = self.datos.pop(0)
>>>>>>> 11127f105247665b71f0a7f30d798859f23012a8
        return self.lanzar_carta
    
    def tamanio(self):
        return len(self.carta)
    
    def mezclar_mazo(self):
        random.shuffle(self.carta)

