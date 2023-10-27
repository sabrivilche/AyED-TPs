from TP1_juego_guerra.modulos.juego_guerra import Mazo, Carta, JuegoGuerra

#Creo las cartas iniciales para cada jugador
cartas_j1 = [Carta(valor, palo) for valor in JuegoGuerra.valor for palo in JuegoGuerra.palo]
cartas_j2 = [Carta(valor, palo) for valor in JuegoGuerra.valor for palo in JuegoGuerra.palo]

#Instancia del juego con las cartas iniciales
juego = JuegoGuerra (semilla = 42, cartas_jugador1 = cartas_j1, cartas_jugador2 = cartas_j2)

#Inicio el juego
ganador = juego.iniciar_juego()

print(f"El ganador de la Guerra es el {ganador}")