<<<<<<< HEAD
from TP1_LDE_testing.modulo import ListaDobleEnlazada
import random
class Mazo:
    def __init__(self):
        self.carta = []
        self.cabeza = None
        self.cola = None
        self.lista = ListaDobleEnlazada()
        self.tamanio = 0

    def vacia(self):
        return len(self.carta) == 0
    
    def poner_abajo(self,dato):#se agrega una sola carta(dato) a la cola
        self.lista.agregar_al_final(dato)
        self.tamanio += 1
    
    # def agregar_cartas(self,dato): #se agrega una lista de cartas al final de la cola self.carta
    #     self.carta.extend(dato)

    def poner_sacar_arriba(self):
        self.lista.agregar_al_inicio()
        self.dato_eliminado = self.lista.extraer(0)
        return self.dato_eliminado
    
    def tamanio(self):
        return len(self.carta)
    
    def mezclar_mazo(self):
        random.shuffle(self.carta)

class Carta: 
    def __init__(self,carta):
        self.carta = carta
        self.valor = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.palo = ['♠', '♥', '♦', '♣']
        self.boca_arriba = None
        self.boca_abajo = None


class JuegoGuerra:
    pass













# from cola import Carta
# import random
# class JuegoGuerra:

#     def __init__(self,semilla):
#         self.mazo_jugador1=Carta()
#         self.mazo_jugador2=Carta()
#         self.semilla=semilla #inicializador del generador de números aleatorios
#         self.Mazo()
#         self.turno=0 #contador de turnos jugador durante la partida

#     def Mazo(self): #método para distribuir las cartas y mezclarlas
#         mazo_completo=list(range(2,15)*4)#Representa las cartas de 2 a A, lo multiplico por 4 para tener el mazo completo
#         random.seed(self.semilla) #inicializo el generador de números aleatorios
#         random.shuffle(mazo_completo) #mezcla las cartas

#         self.mazo_jugador1.agregar_carta(mazo_completo[:26]) #se "reparten" las primeras 26 cartas para el primer jugador y el resto para el segundo 
#         self.mazo_jugador2.agregar_carta(mazo_completo[26:])

#     def jugar_turno(self):
#         self.turno+=1 #incremento el contador para tener el número de turnos jugados
#         carta_judador1=self.mazo_jugador1.sacar_carta #se le saca una carta a ambos jugadores para comenzar el juego
#         carta_judador2=self.mazo_jugador2.sacar_carta

#         if carta_judador1>carta_judador2:
#             self.mazo_jugador1.agregar_carta([carta_judador1,carta_judador2])
        
#         elif carta_judador1<carta_judador2:
#             self.mazo_jugador2.agregar_carta([carta_judador1,carta_judador2])
#         else:
#             self.iniciar_guerra() #si las cartas son iguales comienza la guerra
#         #se comparan las cartas para determinar quien gana el turno

#     def iniciar_guerra(self):
#         cartas_en_mesa=[self.mazo_jugador1.sacar_carta(),self.mazo_jugador2.sacar_carta()]
#         for _ in range(3):
#             if not self.mazo_jugador1.vacia():
#                 cartas_en_mesa.append(self.mazo_jugador1.sacar_carta())
            
#             if not self.mazo_jugador2.vacia():
#                 cartas_en_mesa.append(self.mazo_jugador2.sacar_carta())
            
#             carta_judador1=self.mazo_jugador1.sacar_carta if not self.mazo_jugador1.vacia() else None
#             carta_judador2=self.mazo_jugador2.sacar_carta if not self.mazo_jugador2.vacia() else None

#             if carta_judador1 is not None and carta_judador2 is not None:
#                 cartas_en_mesa.extend([carta_judador1,carta_judador2])
                
#                 if carta_judador1>carta_judador2:
#                     self.mazo_jugador1.agregar_carta(cartas_en_mesa)
                
#                 else:
#                     self.mazo_jugador2.agregar_carta(cartas_en_mesa)
            
#             else:
#                 if carta_judador1 is None: #Un jugador no tiene suficientes cartas para continuar, el otro gana
#                     self.ganador='Jugador 2'
#                 else: 
#                     self.ganador='Jugador 1'
                
#     def jugar_partida(self, max_turnos):
#         self.ganador=None
#         while not self.mazo_jugador1.vacia() and not self.mazo_jugador2.vacia() and self.turno<max_turnos:
#             self.jugar_turno()
        
#         if self.ganador is None:
#             if self.mazo_jugador1.vacia:
#                 self.ganador='Jugador 2'

#             else:
#                 self.ganador='Jugador 1'

#         return self.turno, self.ganador
=======
>>>>>>> 946a70bece8359e67cf585a2a0adc3cb2cf9cb52

