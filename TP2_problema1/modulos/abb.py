# -*- coding: utf-8 -*-
from datetime import datetime#Importo módulo datetime, para manipular fechas y horas

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
class ABB:

    def __init__(self):
        self.raiz =None#inicializo base de datos
        
    def guardar_temperature(self, temperatura,fecha):#Método que guarda nuevas temperaturas en la base de datos
        fecha=datetime.strptime(fecha,'%d/%m/%Y')#Convertimos la fecha (string), a un objeto datetime,
        #así comparamos fechas más eficientemente
        self.raiz.insert(fecha,temperatura)#Insertamos la temperatura en la base de datos, usando la fecha como clave

    def devolver_temperatura(self,fecha):#Método para obtener un temperatura de una fecha específica
        fecha=datetime.strptime(fecha,'%d/%m/%Y')
        returnself.raiz.find(fecha)#Buscamos la temperatura de la fecha específica en la base de datos y la devolvemos

    def max_temp_rango(self,fecha1,fecha2):
        fecha1=datetime.strptime(fecha1,'%d/%m/%Y')
        fecha2=datetime.strptime(fecha2,'%d/%m/%Y')
        return self.raiz.find.max(fecha1,fecha2)#Buscamos la tempertura máxima en el rango especificado y
        #lo devolvemos

    def min_temp_rango(self,fecha1,fecha2):
        fecha1=datetime.strptime(fecha1,'%d/%m/%Y')
        fecha2=datetime.strptime(fecha2,'%d/%m/%Y')
        return self.raiz.find.min(fecha1,fecha2)

    def temp_extremos_rango(self,fecha1,fecha2):
        return self.min_temp_rango(fecha1,fecha2), self.max_temp_rango(fecha1,fecha2)
    
    def borrar_temperatur(self,fecha):
        fecha=datetime.strptime(fecha,'%d/%m/%Y')
        self.raiz.delete(fecha)
    
    def devolver_temperaturas(self,fecha1,fecha2):
        fecha1=datetime.strptime(fecha1,'%d/%m/%Y')
        fecha2=datetime.strptime(fecha2,'%d/%m/%Y')
        temperaturas=self.raiz.find.range(fecha1,fecha2)

        return [f'{fecha.strftime("%d/%m/%Y")}: {temp} ºC' for fecha, temp in temperaturas]
    
    def cantidad_muestras(self):
        return self.raiz.size()

    def agregar(self, clave, valor):#método para agregar una nueva clave y valor al árbol
            if self.raiz is None:#si el árbol está vacío
                self.raiz = Nodo(clave, valor)#crea un nuevo nodo y lo establece como la raíz
            else:#si no está vacío 
                self._agregar(clave, valor, self.raiz)#llama al método _agregar
                #que agrega recursivamene el nuevo nodo en la posición correcta del árbol

    def _agregar(self, clave, valor, nodo):
        if clave < nodo.clave:#comprueba  si la clave que se va a agregar es menor que la clave del nodo actual
            if nodo.hijoIzquierdo is None:#si la clave es menor y el nodo actual no tiene un hijo izquierdo, entonces:
                nodo.hijoIzquierdo = Nodo(clave, valor)#crea un nuevo nodo con la clave y el valor dado, y lo asigna
                #como el hijo izquierdo del nodo actual
            
            else:#si el nodo actual ya tiene un hijo izquierdo:
                self._agregar(clave, valor, nodo.hijoIzquierdo)#llama a la función _agregar de nuevo
                #pero esta vez con el hijo izquierdo del nodo actual como el nuevo nodo actual
        
        else:#si la clave que se va a agregar no es menor que la clave del nodo actual(es mayor o igual)
            if nodo.hijoDerecho is None:#y si el nodo actul no tiene un hijo derecho
                nodo.hijoDerecho = Nodo(clave, valor)#crea un nuevo nodo con la clave y el valor dado, y lo asigna
                #como el hijo derecho del nodo actual
            else:#si el nodo actual ya tiene un hijo derecho:
                self._agregar(clave, valor, nodo.hijoDerecho)#llama a la función _agregar de nuevo, pero con el hijo derecho
                #del nodo actual como el nuevo nodo actual