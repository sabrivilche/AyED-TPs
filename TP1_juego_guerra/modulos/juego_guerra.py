from cola import Cola
class JuegoGuerra:

    def __init__(self,semilla):
        self.mazo_jugador1=Cola()
        self.mazo_jugador2=Cola()
        self.semilla=semilla
        self.inicializar_mazos()
        self.turno=0

    def inicializar_mazos(self):
        mazo_completo=list(range(2,15)*4)#Representa las cartas de 2 a A (sin palos)
        random.seed(self.semilla)
        random.shuffle(mazo_completo)

        self.mazo_jugador1.agregar_carta(mazo_completo[:26])
        self.mazo_jugador2.agregar_carta(mazo_completo[26:])

    def jugar_turno(self):
        self.turno+=1
        carta_judador1=self.mazo_jugador1.sacar_carta
        carta_judador2=self.mazo_jugador2.sacar_carta

        if carta_judador1>carta_judador2:
            self.mazo_jugador1.agregar_carta([carta_judador1,carta_judador2])
        
        elif carta_judador1<carta_judador2:
            self.mazo_jugador2.agregar_carta([carta_judador1,carta_judador2])
        else:
            self.iniciar_guerra()

    def iniciar_guerra(self):
        cartas_en_mesa=[self.mazo_jugador1.sacar_carta(),self.mazo_jugador2.sacar_carta()]
        for _ in range(3):
            if not self.mazo_jugador1.vacia():
                cartas_en_mesa.append(self.mazo_jugador1.sacar_carta())
            
            if not self.mazo_jugador2.vacia():
                cartas_en_mesa.append(self.mazo_jugador2.sacar_carta())
            
            carta_judador1=self.mazo_jugador1.sacar_carta if not self.mazo_jugador1.vacia() else None
            carta_judador2=self.mazo_jugador2.sacar_carta if not self.mazo_jugador2.vacia() else None

            if carta_judador1 is not None and carta_judador2 is not None:
                cartas_en_mesa.extend([carta_judador1,carta_judador2])
                
                if carta_judador1>carta_judador2:
                    self.mazo_jugador1.agregar_carta(cartas_en_mesa)
                
                else:
                    self.mazo_jugador2.agregar_carta(cartas_en_mesa)
            
            else:
                if carta_judador1 is None: #Un jugador no tiene suficientes cartas para continuar, el otro gana
                    self.ganador='Jugador 2'
                else: 
                    self.ganador='Jugador 1'
                
    def jugar_partida(self, max_turnos):
        self.ganador=None
        while not self.mazo_jugador1.vacia() and not self.mazo_jugador2.vacia() and self.turno<max_turnos:
            self.jugar_turno()
        
        if self.ganador is None:
            if self.mazo_jugador1.vacia:
                self.ganador='Jugador 2'

            else:
                self.ganador='Jugador 1'

        return self.turno, self.ganador
