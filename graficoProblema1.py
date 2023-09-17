import random
import time
import matplotlib.pyplot as plt
from TP1_LDE_testing.modulo import ListaDobleEnlazada
from TP1_LDE_testing.Nodo import Nodo
def generar_lista_aleatoria(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Función para medir el tiempo de ejecución del algoritmo de ordenamiento
def medir_tiempo_ordenamiento(n):
    lista = generar_lista_aleatoria(n)
    inicio = time.time()
    lista_doble_ordenada = ListaDobleEnlazada()
    for item in lista:
        lista_doble_ordenada.agregar(item)
    lista_doble_ordenada.ordenar()
    fin = time.time()
    return fin - inicio

# Tamaños de entrada (n)
tamanos = [10, 100, 1000, 10000, 20000, 30000]

# Medir el tiempo de ejecución para cada tamaño
tiempos = []
for n in tamanos:
    tiempo = medir_tiempo_ordenamiento(n)
    tiempos.append(tiempo)

# Graficar los resultados
plt.plot(tamanos, tiempos, marker='o')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento del algoritmo QuickSort')
plt.grid(True)
plt.show()
