# -*- coding: utf-8 -*-

from random import randint

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
        with open("datos.txt", 'a+') as archivo:
            archivo.writelines(bloque)
            
crear_archivo_de_datos('datos.txt')

def mezcla_directa(nombre):
    B=1000
    # Leer el archivo y dividirlo en bloques de B claves
    bloques = [] #almacenará los bloques de claves ordenadas
    with open('datos.txt', 'r') as archivo: 
        bloque = [] #almacena las claves del bloque actual
        for linea in archivo:
            bloque.append(int(linea.strip())) #elimina los espacios en blanco, convierte los valores en enteros y los agrega a la lista bloque
            if len(bloque) == B: 
                bloques.append(sorted(bloque)) #se ordena el bloque y se agrega a la lista bloques
                bloque = [] #reinicio la lista bloque
        if bloque: #si bloque no está vacío
            bloques.append(sorted(bloque)) #se ordenan las claves que quedaban y se agregan a la lista bloques

    # Ordenar los bloques y escribirlos en el archivo
    with open('datos.txt', 'w') as archivo:
        for bloque in bloques: #itera sobre cada bloque dentro de bloques
            for clave in bloque: #itera sobre cada clave dentro de bloque
                archivo.write(str(clave) + '\n') #se escribe cada clave en el archivo como cadena de texto

def verificar_ordenamiento(nombre):
    # Leer el archivo y verificar que las claves estén ordenadas
    claves = []
    with open('datos.txt', 'r') as archivo:
        for linea in archivo:
            claves.append(int(linea.strip()))
    return claves == sorted(claves) #lee las claves del archivo y las compara con una versión ordenada, si están ordenadas = True, de lo contrario = False


#ordenar_archivo=mezcla_directa('datos.txt')
#verificacion=verificar_ordenamiento(ordenar_archi)
