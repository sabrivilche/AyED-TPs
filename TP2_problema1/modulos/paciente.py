# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]#Inicializa el montículo con una lista que contiene un solo elemento, 
        #esto es para simplificar otros métodos al permitirles asumir que el índice 0 no se utiliza
        self.tamanoActual = 0

    def infiltArriba(self, i):#El método infiltArriba se utiliza para mantener la propiedad del montículo después de insertar un nuevo elemento
        while i // 2 > 0:
            if self.listaMonticulo[i].get_riesgo() < self.listaMonticulo[i // 2].get_riesgo():#Compara el nuevo elemento con su padre 
                #si el nuevo elemento es menor,lo intercambia. Cotinúa hasta que el elemento esté en una posicion mayor a la del padre 
                aux = self.listaMonticulo[i // 2]#Sucede el intercambio
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]#El padre pasa a ser el nuvo elemento
                self.listaMonticulo[i] = aux#El que era el padre pasa a ser el hijo
            i = i // 2

    def insertar(self, paciente):#Añade un nuevo elemento al final del montículo 
        self.listaMonticulo.append(paciente)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)#luego llama a infiltArriba para asegurarse de que el montículo siga siendo un montículo.

    def infiltAbajo(self, i):#Se utiliza para mantener la propiedad del montículo luego de eliminar la raíz
        while (i * 2) <= self.tamanoActual:
            hijo_menor = self.hijoMin(i)
            if self.listaMonticulo[i].get_riesgo() > self.listaMonticulo[hijo_menor].get_riesgo():#Compara la nueva raíz (último elemento del árbol)
                # con sus hijos, y si es mayor que cualquiera de ellos, los intercambia. Continúa haciendo esto hasta que elemento esté en una posicion donde es menor que sus hijos
                aux = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hijo_menor]
                self.listaMonticulo[hijo_menor] = aux
            i = hijo_menor#Luego, se mueve al hijo y repite el proceso hasta que llega a una hoja del montículo

    def hijoMin(self, i): #Devuelve el índice del hijo que es menor de un nodo
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2].get_riesgo() < self.listaMonticulo[i * 2 + 1].get_riesgo():
                #Si el nodo solo tiene un hijo(está en el índice tamanoActual//2)
                return i * 2#devuelve ese hijo
            else:#De lo contrario, devuelve el hijo con el valor más pequeño
                return i * 2 + 1

    def eliminarMin(self):#Elimina y devuelve la raíz del montículo (el elemento más pequeño)
        valor_eliminado = self.listaMonticulo[1]#Guarda el valor de la raíz
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]#reemplaza la raíz con el último elemento del montículo
        self.tamanoActual = self.tamanoActual - 1#Disminuye el tamaño del montículo en 1
        self.listaMonticulo.pop()#Elimina el último elemento de la lista
        self.infiltAbajo(1)#Llama inflitAbajo para restaurar la propiedad del montpiculo
        return valor_eliminado

    def construirMonticulo(self, unaLista): #Construye un montículo a partir de una lista de elementos
        i = len(unaLista) // 2#Comienza en el medio de la lista (padre del último elelemnto de la list)
        self.tamanoActual = len(unaLista)#Inicializa tamaño con la cantidad de elemento de la lista
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)#Llamando a infiltAbajo para cada elemento
            i = i - 1#comienza a moverse hacia atrás. Esto asegura que cada subárbol es un montículo antes de que infiltAbajo se llame en su padre,
            #lo que a su vez asegura que cada subárbol más grande también es un montículo
        
        
        