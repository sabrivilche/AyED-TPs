from TP2_problema3.modulo import Grafo, dijkstra_max_weight, dijkstra_min_cost

grafo = Grafo()#Crea el grafo con los datos que están dentro del archivo "rutas.txt"
with open("rutas.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        #separo los datos por ","
        elementos = linea.strip().split(",")

        ciudad_origen = elementos[0]
        ciudad_destino = elementos[1]
        peso = int(elementos[2])
        precio = int(elementos[3])

        grafo.agregarArista(ciudad_origen, ciudad_destino, peso, precio)

start_city = 'CiudadBs.As.'
end_city = 'Mendoza' 

max_weight = dijkstra_max_weight(grafo, start_city, end_city)
print(f'El peso máximo desde {start_city} a {end_city} es: {max_weight}')

min_cost=dijkstra_min_cost(grafo, start_city, end_city)
print(f'El precio mínimo desde {start_city} a {end_city} es: {min_cost}')