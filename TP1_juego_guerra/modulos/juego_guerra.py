from TP1_LDE_testing.modulo import ListaDobleEnlazada
import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        self.boca_arriba = False #considero que todas las cartas están boca abajo cuando comienza el juego

    def __str__(self):
        return f"{self.valor}{self.palo}"

class Mazo:
    def __init__(self, mazo=None):
        if mazo is None:
            mazo = []
        self.tamanio = 0
        self.mazo = ListaDobleEnlazada()

    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta)
        self.tamanio += 1
    
    def poner_arriba(self,carta):
        self.mazo.agregar_al_inicio(carta)
    
    def sacar_arriba(self):
        if not self.mazo.vacia():
            return self.mazo.extraer(0)

    def esta_vacio(self):
        return self.mazo.vacia()

class JuegoGuerra:
    valor = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palo = ['♠', '♥', '♦', '♣']
    def __init__(self, semilla, cartas_jugador1, cartas_jugador2):
        self.cartas_jugador1 = Mazo(cartas_jugador1)
        self.cartas_jugador2 = Mazo(cartas_jugador2)
        self.turno = 0
        self.max_turnos = 10000  # Número máximo de turnos para evitar bucles infinitos

        random.seed(semilla) #genero números aleatorios

    def iniciar_juego(self):
        while not self.cartas_jugador1.esta_vacio() and not self.cartas_jugador2.esta_vacio() and self.turno < self.max_turnos: #mientras ninguno de los 2 jugadores se quede sin cartas y no se pasen del número de turnos
            self.turno += 1
            carta_jugador1 = self.cartas_jugador1.poner_sacar_arriba() #se saca la carta de arriba del mazo de cada jugador y se almacena en carta_jugador
            carta_jugador2 = self.cartas_jugador2.poner_sacar_arriba()

            # Comparar las cartas
            if self.comparar_cartas(carta_jugador1, carta_jugador2): #si la comparación la gana el jugador 1 las cartas se ponen en la parte inferior del mazo
                self.cartas_jugador1.poner_abajo(carta_jugador1)
                self.cartas_jugador1.poner_abajo(carta_jugador2)
            else: #si la comparación la gana el jugador 2
                self.cartas_jugador2.poner_abajo(carta_jugador1)
                self.cartas_jugador2.poner_abajo(carta_jugador2)

        if self.turno == self.max_turnos:
            return "Empate" #si se alcanza la cantidad límite de turnos se considera un empate
        elif self.cartas_jugador1.esta_vacio():
            return "Jugador 2" #si el mazo del jugador 1 está vacio se considera como ganador el jugador 2
        else:
            return "Jugador 1"

    def comparar_cartas(self, carta1, carta2):
        valores_cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        valor_carta1 = valores_cartas.index(carta1.valor) #se comparan los valores de cada carta
        valor_carta2 = valores_cartas.index(carta2.valor)
        return valor_carta1 > valor_carta2 #si la carta1 es mayor que la carta2 retorna True, de lo contrario False

