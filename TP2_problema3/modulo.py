import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []
        self.indice = 0

    def insertar(self, clave, prioridad):#Inserta un elemento en la cola con una clave y una prioridad 
        heapq.heappush(self.cola, (prioridad, self.indice, clave))
        self.indice += 1

    def obtener(self):#Elimina y devuelve el elemento con la mayor prioridad de la cola
        return heapq.heappop(self.cola)[-1]

    def esta_vacia(self):
        return not bool(self.cola)

    def decrementar_clave(self, clave, nueva_prioridad):#Este método disminuye la prioridad de un elemento si se encuentra una ruta de transporte más eficiente
        for i, (prioridad, _, c) in enumerate(self.cola):
            if c == clave:
                self.cola[i] = (nueva_prioridad, self.indice, clave)
                self.indice += 1
                heapq.heapify(self.cola)
                break

class Vertice:
    def __init__(self, clave):
        self.id = clave#almacena clave o id unico
        self.conectadoA = {}#diccionario que almacena vecinos y sus ponderaciones y precios
        self.distancia = 0#se buscara la distancia mas corta con un algoritmo
        self.predecesor = None#se usará para rastrear el predecesor en un camino
        self.precio=float('inf')# para representar un precio desconocido o no calculado

    def agregarVecino(self, vecino, ponderacion=0,precio=0):
        self.conectadoA[vecino] = (ponderacion,precio)

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, predecesor):# para rastrear el camino más corto entre otros caminos
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def __str__(self):
        return str(self.id)

    def obtenerConexiones(self):
        return self.conectadoA.keys()#Devuelve todos los vértices vecinos del vértice actual

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
        self.listaVertices[clave] = nuevoVertice#Lo añade al diccionario y aumenta el contador
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):#Verifica si la clave está en el grafo
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0,precio=0):#Agrega una arista al grafo. Las claves de los vértices de origen(de) y destino(a) se pasan como argumento,
        #junto con el costo y el precio.
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:#Si alguno de los vértices no existe en el grafo, se crea un nuevo vértice
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo,precio)

    def obtenerVertices(self):#Devuelve todas las claves de los vértices en el grafo
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

def dijkstra_max_weight(graph, start_city, end_city):
    cola = ColaPrioridad()
    distancias = {city: float("-inf") for city in graph.listaVertices}#Asigna a cada ciudad distancia inicial de menos infinito, excepto la ciudad de inicio
    distancias[start_city] = float("inf")
    cola.insertar(start_city, float("inf"))

    while not cola.esta_vacia():#Mientras no esté vacía
        current_city = cola.obtener()#obtiene la ciudad con la mayor distancia
        if current_city == end_city:#Si es la ciudad final devuelve la distancia
            return distancias[current_city], construir_camino(predecesores, start_city, end_city)

        current_vertex = graph.listaVertices[current_city]

        for neighbor in current_vertex.obtenerConexiones():#Para cada vecino de la ciudad actual
            neighbor_city = neighbor.id
            weight = current_vertex.obtenerPonderacion(neighbor)
            possible_weight = min(distancias[current_city], weight)#calcula el posible peso como el mínimo entre la distancia actual a la ciudad y el peso de la arista a ese vecino
            if possible_weight > distancias[neighbor_city]:#Si este peso posible es mayor que la distancia actual al vecino
                distancias[neighbor_city] = possible_weight#Actualiza la distancia del vecino
                predecesores[neighbor_city] = current_city
                cola.insertar(neighbor_city, possible_weight)#Lo inserta en la cola de prioridad

    return float("-inf"), []

def dijkstra_min_cost(graph, start_city, end_city):
    cola = ColaPrioridad()
    costos = {city: float("inf") for city in graph.listaVertices}#Asigna a cada ciudad un costo inicial infinito
    predecesores = {city: None for city in graph.listaVertices}
    costos[start_city] = 0 #Ciudad de inicio tiene un costo de cero
    cola.insertar(start_city, 0)

    while not cola.esta_vacia():#Mientras la cola no esté vacía
        current_city = cola.obtener()#Obtiene la ciudad con el menor costo
        if current_city == end_city:#Si es la ciudad final, devuelve el costo
            return costos[current_city], construir_camino(predecesores, start_city, end_city)

        current_vertex = graph.listaVertices[current_city]#Se obtiene el vértice correspondiente a la ciudad actual


        for neighbor in current_vertex.obtenerConexiones():#Para cada vecino de la ciudad actual
            neighbor_city = neighbor.id
            cost = current_vertex.obtenerPrecio(neighbor)  #devuelve el precio de la arista
            possible_cost = costos[current_city] + cost
            if possible_cost < costos[neighbor_city]:#Si el posible costo es menor que el costo actual al vecino 
                costos[neighbor_city] = possible_cost#Actualiza el costo del vecino
                predecesores[neighbor_city] = current_city
                cola.insertar(neighbor_city, -possible_cost)#Lo inserta en la cola de prioridad

    return float("inf"), []


def construir_camino(predecesores, start_city, end_city):
    camino = []
    actual = end_city
    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    return camino