class Cola:
    def __init__(self):
        self.datos = []
        self.tamanio = 0

    def vacia(self):
        return self.datos == None
    
    def agregar_carta(self,dato):
        self.datos.append(dato)
        self.tamanio += 1

    def sacar_carta(self):
        self.lanzar_carta = self.datos.pop()
        return self.lanzar_carta
    
    def tamanio(self):
        return len(self.datos)
