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
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
            
crear_archivo_de_datos('datos.txt')

def mezcla_directa(nombre):
    # Leer el archivo y dividirlo en bloques de B claves
    bloques = []
    with open(nombre, 'r') as archivo:
        bloque = []
        for linea in archivo:
            bloque.append(int(linea.strip()))
            if len(bloque) == B:
                bloques.append(sorted(bloque))
                bloque = []
        if bloque:
            bloques.append(sorted(bloque))

    # Ordenar los bloques y escribirlos en el archivo
    with open(nombre, 'w') as archivo:
        for bloque in bloques:
            for clave in bloque:
                archivo.write(str(clave) + '\n')

def verificar_ordenamiento(nombre):
    # Leer el archivo y verificar que las claves estén ordenadas
    claves = []
    with open(nombre, 'r') as archivo:
        for linea in archivo:
            claves.append(int(linea.strip()))
    return claves == sorted(claves)