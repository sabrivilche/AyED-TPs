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
    B = 1000 # tamaño del bloque
    bloques = [] # almacenará los bloques de claves ordenadas
    archivo_entrada = open(nombre, 'r')
    archivo_salida = open('salida.txt', 'w')
    archivo_salida.close()
    i = 0
    while True:
        bloque = []
        for j in range(B):
            linea = archivo_entrada.readline()
            if not linea:
                break
            bloque.append(int(linea.strip()))
        if not bloque:
            break
        bloques.append(bloque)
        i += 1
    archivo_entrada.close()

    while len(bloques) > 1:
        bloque1 = bloques.pop(0)
        bloque2 = bloques.pop(0)
        resultado = []
        i = j = 0
        while i < len(bloque1) and j < len(bloque2):
            if bloque1[i] < bloque2[j]:
                resultado.append(bloque1[i])
                i += 1
            else:
                resultado.append(bloque2[j])
                j += 1
        resultado += bloque1[i:]
        resultado += bloque2[j:]
        bloques.append(resultado)

    with open('salida.txt', 'a') as archivo_salida:
        for clave in bloques[0]:
            archivo_salida.write(str(clave) + '\n')
 
def verificar_ordenamiento(nombre):
    # Leer el archivo y verificar que las claves estén ordenadas
    claves = []
    with open('datos.txt', 'r') as archivo:
        for linea in archivo:
            claves.append(int(linea.strip()))
    return claves == sorted(claves) #lee las claves del archivo y las compara con una versión ordenada, si están ordenadas = True, de lo contrario = False


#ordenar_archivo=mezcla_directa('datos.txt')
#verificacion=verificar_ordenamiento(ordenar_archi)
