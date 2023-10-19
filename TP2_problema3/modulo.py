import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []
        self.indice = 0

    def insertar(self, clave, prioridad):
        heapq.heappush(self.cola, (prioridad, self.indice, clave))
        self.indice += 1

    def obtener(self):
        return heapq.heappop(self.cola)[-1]

    def esta_vacia(self):
        return not bool(self.cola)

    def decrementar_clave(self, clave, nueva_prioridad):
        for i, (prioridad, _, c) in enumerate(self.cola):
            if c == clave:
                self.cola[i] = (nueva_prioridad, self.indice, clave)
                self.indice += 1
                heapq.heapify(self.cola)
                break

class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = 0
        self.predecesor = None
        self.precio=float('inf')#Agrego atributo precio
    def agregarVecino(self, vecino, ponderacion=0,precio=0):
        self.conectadoA[vecino] = (ponderacion,precio)#Guardamos el precio junto con la ponderación

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def __str__(self):
        return str(self.id)

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino][0]

    def obtenerPrecio(self,vecino):
        return self.conectadoA[vecino][1]
    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0,precio=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo,precio)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())



def dijkstra_max_weight(graph, start_city, end_city):
    cola = ColaPrioridad()
    distancias = {city: float("-inf") for city in graph.listaVertices}
    distancias[start_city] = float("inf")
    cola.insertar(start_city, float("inf"))

    while not cola.esta_vacia():
        current_city = cola.obtener()
        if current_city == end_city:
            return distancias[current_city]

        current_vertex = graph.listaVertices[current_city]

        for neighbor in current_vertex.obtenerConexiones():
            neighbor_city = neighbor.id
            weight = current_vertex.obtenerPonderacion(neighbor)
            possible_weight = min(distancias[current_city], weight)
            if possible_weight > distancias[neighbor_city]:
                distancias[neighbor_city] = possible_weight
                cola.insertar(neighbor_city, possible_weight)

    return float("-inf")

grafo = Grafo()#Crea el grafo con los datos que están dentro del archivo "rutas.txt"
with open("rutas.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        #separo los datos por ,
        elementos = linea.strip().split(",")

        
        ciudad_origen = elementos[0]
        ciudad_destino = elementos[1]
        peso = int(elementos[2])
        precio = int(elementos[3])

        # Agrego la arista
        grafo.agregarArista(ciudad_origen, ciudad_destino, peso, precio)

start_city = 'CiudadBs.As.'
end_city = 'VillaMercedes' 

max_weight = dijkstra_max_weight(grafo, start_city, end_city)
print(f'El peso máximo desde {start_city} a {end_city} es: {max_weight}')
