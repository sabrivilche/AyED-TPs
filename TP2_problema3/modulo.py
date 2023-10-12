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

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

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
        return self.conectadoA[vecino]

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

    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

def dijkstra_max_bottleneck(graph, start, end):
    cp = ColaPrioridad()
    start_vertex = graph.obtenerVertice(start)
    start_vertex.asignarDistancia(float('inf'))
    cp.insertar(start_vertex, -start_vertex.obtenerDistancia())

    while not cp.esta_vacia():
        vertex_actual = cp.obtener()

        for vertex_siguiente in vertex_actual.obtenerConexiones():
            nueva_distancia = min(vertex_actual.obtenerDistancia(), vertex_actual.obtenerPonderacion(vertex_siguiente))

            if nueva_distancia > vertex_siguiente.obtenerDistancia():
                vertex_siguiente.asignarDistancia(nueva_distancia)
                vertex_siguiente.asignarPredecesor(vertex_actual)
                cp.decrementar_clave(vertex_siguiente, -nueva_distancia)

    end_vertex = graph.obtenerVertice(end)
    max_bottleneck = end_vertex.obtenerDistancia()

    return max_bottleneck


if __name__ == "__main__":
    graph = Grafo()

    # Crear un conjunto para almacenar todas las ciudades
    ciudades = set()

    # Leo los datos dentro de ruta y creo el grafo
    with open("rutas.txt", 'r') as file:
        for line in file:
            start, end, capacity, price = line.strip().split(',')
            capacity = int(capacity)
            ciudades.add(start)
            ciudades.add(end)
            graph.agregarArista(start, end, capacity)

    start_city = "CiudadBs.As."

    # Calcular el mayor peso desde bs as a la otra ciudad
    for end_city in ciudades:
        if start_city != end_city:
            max_bottleneck = dijkstra_max_bottleneck(graph, start_city, end_city)
            print(f"El peso máximo que se puede transportar desde {start_city} a {end_city} es {max_bottleneck} kg.")


