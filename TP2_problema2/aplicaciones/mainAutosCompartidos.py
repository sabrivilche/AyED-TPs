# -*- coding: utf-8 -*-
from datetime import datetime
from TP2_problema2.modulos.abb import ABB

abb = ABB()

abb.guardar_temperatura(25.5, "30/09/2023")
abb.guardar_temperatura(28.2, "30/09/2023")
abb.guardar_temperatura(22.8, "30/09/2023")

fecha1 = "30/09/2023"
fecha2 = "30/09/2023"

print("Temperaturas en el rango de fechas: ")

for i in abb.devolver_temperaturas(fecha1, fecha2):
    print(i)

print("Cantidad de muestras: ", abb.cantidad_muestras())