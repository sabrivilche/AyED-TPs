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
end_city = input("Ingresa la ciudad de destino: ")  

max_weight, camino_max = dijkstra_max_weight(grafo, start_city, end_city)
print(f'El peso máximo desde {start_city} a {end_city} es: {max_weight}')
print(f'Camino para peso máximo: {" -> ".join(camino_max)}')

min_cost, camino_min = dijkstra_min_cost(grafo, start_city, end_city)
print(f'El precio mínimo desde {start_city} a {end_city} es: {min_cost}')
print(f'Camino para precio mínimo: {" -> ".join(camino_min)}')