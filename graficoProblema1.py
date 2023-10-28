import random
import timeit
import matplotlib.pyplot as plt
from TP1_LDE_testing.modulo import ListaDobleEnlazada
from TP1_LDE_testing.Nodo import Nodo

def generar_lista_aleatoria(n):#Genera una lista de números aleatorios
    return [random.randint(1, 1000) for _ in range(n)]

def medir_tiempo_ordenamiento(lista):#Mide el tiempo que tarda en ordenarse la lista
    inicio = timeit.default_timer()
    lista.ordenar()
    fin = timeit.default_timer()
    return fin - inicio#Calcula y devuelve el tiempo total que tardó en ordenarse la lista
#Tamaños para las listas que se van a generar y ordenar
tamanios = [10, 100,250,500,750, 1000,1500,2000,2500,3000,3500,4000,4500,5000]
tiempos = []

for n in tamanios:
    lista = ListaDobleEnlazada()
    lista_datos = generar_lista_aleatoria(n)#Genera una lista aleatoria de tamaño n
    for dato in lista_datos:#Recorre cada dato en la lista aleatoria generada
        lista.agregar_al_final(dato)
    
    tiempo_ejecucion = medir_tiempo_ordenamiento(lista)
    tiempos.append(tiempo_ejecucion)

plt.plot(tamanios, tiempos, marker='o', linestyle='-')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Medición de Tiempos de Ejecución del Método QuickSort')
plt.grid(True)
plt.show()