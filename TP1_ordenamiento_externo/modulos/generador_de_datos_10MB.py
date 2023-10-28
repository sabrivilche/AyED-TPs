# -*- coding: utf-8 -*-

from random import randint
import heapq
import os

def crear_archivo_de_datos(nombre):
    f = 10**5
    N = 5*f
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
            
crear_archivo_de_datos('datos.txt')

def ordenamiento(entrada, salida, bloque_size):
    
    bloques_mem = [] # Lista para almacenar los bloques ordenados en memoria

    # Abrir el archivo de entrada para lectura
    with open(entrada, 'r') as file_entrada:
        bloque = []
        for linea in file_entrada:
            bloque.append(int(linea))
            if len(bloque) == bloque_size:
                bloque.sort()
                bloques_mem.append(bloque)
                bloque = []
        
        if bloque:
            bloque.sort()
            bloques_mem.append(bloque)

    # Fusiona los bloques ordenados
    with open(salida, 'w') as file_salida:        
        heap = [(bloque[0], i, 0) for i, bloque in enumerate(bloques_mem) if bloque] # Inicializa un heap con el primer elemento de cada bloque
        
        heapq.heapify(heap) # Convertir la lista en un heap (min-heap)

        while heap:
            valor, bloque_idx, elemento_idx = heapq.heappop(heap)
            file_salida.write(str(valor) + '\n')
            
            elemento_idx += 1 # Avanzar al siguiente elemento en el bloque actual

            # Si el bloque actual tiene más elementos, agregar el siguiente elemento al heap
            if elemento_idx < len(bloques_mem[bloque_idx]):
                heapq.heappush(heap, (bloques_mem[bloque_idx][elemento_idx], bloque_idx, elemento_idx))

def comprobar_tamano_archivos(archivo1, archivo2): #Compruebo que el archivo "datos.txt" y el archivo "salida.txt" tengan el mismo tamaño
    return os.path.getsize(archivo1) == os.path.getsize(archivo2)

def comprobar_ordenamiento_archivo(archivo): #Compruebo si el archivo "salidas.txt" está correctamente ordenado
    prev_valor = float('-inf')
    with open(archivo, 'r') as file:
        for linea in file:
            valor = int(linea)
            if valor < prev_valor:
                return False
            prev_valor = valor
    return True

# Parámetros para el ordenamiento externo
archivo_entrada_no_ordenado = 'datos.txt'
archivo_salida_ordenado = 'salida.txt'
tamano_bloque = 10000  # Tamaño del bloque en memoria

# Aplico el ordenamiento externo
ordenamiento(archivo_entrada_no_ordenado, archivo_salida_ordenado, tamano_bloque)
print(f'Archivo ordenado: {archivo_salida_ordenado}')

if comprobar_tamano_archivos(archivo_entrada_no_ordenado, archivo_salida_ordenado):
    print("El tamaño de los archivos es el mismo.")

# Comprobar si el archivo ordenado está en orden
if comprobar_ordenamiento_archivo(archivo_salida_ordenado):
    print("El archivo ordenado está en orden.")
else:
    print("El archivo ordenado no está en orden.")
