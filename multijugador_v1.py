class tictactoe():
  def __init__(self):
    self.tablero = [[' ','A', 'B', 'C'], ['1', ' ', ' ', ' '], ['2', ' ', ' ', ' '], ['3', ' ', ' ', ' ']]
    self.jugador1 = ''
    self.jugador2 = ''
    self.hay_ganador = False
    self.turno = 1
    self.lista_posiciones = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

  def iniciar_partida(self):
    self.j1 = str(input('Ingrese nombre del jugador 1: '))
    self.j2 = str(input('Ingrese nombre del jugador 2: '))

    print('\n')

    simbolo = input(self.j1 + ', elige el número del símbolo escogido:\n1. X \n2. O\n')
    while simbolo != '1' and simbolo != '2' or str(simbolo).isalpha() == True:
      simbolo = input(self.j1 + ', elige un número válido:\n1. X \n2. O\n')
    if simbolo == '1':
      self.jugador1 = 'X'
      self.jugador2 = 'O'
    else:
      self.jugador1 = 'O'
      self.jugador2 = 'X'

  def juega_jugador1(self):
    posicion = input(self.j1 + ', escoge una posición, de la forma "A1" o "a1": ')

    while posicion.lower() not in self.lista_posiciones:
      posicion = input(self.j1 + ', escoge otra posición válida, de la forma "A1" o "a1": ')


    if posicion[0].lower() == 'a':
      self.tablero[int(posicion[1])][1] = self.jugador1

    elif posicion[0].lower() == 'b':
      self.tablero[int(posicion[1])][2] = self.jugador1

    elif posicion[0].lower() == 'c':
      self.tablero[int(posicion[1])][3] = self.jugador1

    self.turno = 2
    self.lista_posiciones.remove(posicion.lower())
    print('\n')




  def juega_jugador2(self):
    posicion = input(self.j2 + ', escoge una posición, de la forma "A1" o "a1": ')

    while posicion.lower() not in self.lista_posiciones:
      posicion = input(self.j2 + ', escoge otra posición válida, de la forma "A1" o "a1": ')

    if posicion[0].lower() == 'a':
      self.tablero[int(posicion[1])][1] = self.jugador2

    elif posicion[0].lower() == 'b':
      self.tablero[int(posicion[1])][2] = self.jugador2

    elif posicion[0].lower() == 'c':
      self.tablero[int(posicion[1])][3] = self.jugador2

    self.turno = 1
    self.lista_posiciones.remove(posicion.lower())
    print('\n')
    


  def imprimir_tablero(self):
    for fila in self.tablero:
      print(fila)
    
  def verificar_ganador(self):
    for i in range(1, 4):
      if self.tablero[i][1] == self.tablero[i][2] == self.tablero[i][3] and self.tablero[i][1] != ' ':
        if self.tablero[i][1] == self.jugador1:
          print('¡Felicitaciones, ha ganado', self.j1 + '!')
          
        else:
          print('¡Felicitaciones, ha ganado', self.j2 + '!')

        self.hay_ganador = True

    for i in range(1, 4):
      if self.tablero[1][i] == self.tablero[2][i] == self.tablero[3][i] and self.tablero[1][i] != ' ':
        if self.tablero[1][i] == self.jugador1:
          print('¡Felicitaciones, ha ganado', self.j1 + '!')
          
        else:
          print('¡Felicitaciones, ha ganado', self.j2 + '!')

        self.hay_ganador = True

    if self.tablero[1][1] == self.tablero[2][2] == self.tablero[3][3] and self.tablero[1][1] != ' ':
        if self.tablero[1][1] == self.jugador1:
          print('¡Felicitaciones, ha ganado', self.j1 + '!')
          
        else:
          print('¡Felicitaciones, ha ganado', self.j2 + '!')

        self.hay_ganador = True

    
    if self.tablero[1][3] == self.tablero[2][2] == self.tablero[3][1] and self.tablero[1][3] != ' ':
        if self.tablero[1][3] == self.jugador1:
          print('¡Felicitaciones, ha ganado', self.j1 + '!')

        else:
          print('¡Felicitaciones, ha ganado', self.j2 + '!')

        self.hay_ganador = True

    if len(self.lista_posiciones) == 0:
      print('Empate')
      self.hay_ganador = True


  

partida = tictactoe()
partida.iniciar_partida()
print('\n')
partida.imprimir_tablero()
while partida.hay_ganador == False:
  if partida.turno == 1:
    partida.juega_jugador1()
    
  elif partida.turno == 2:
    partida.juega_jugador2()

  partida.verificar_ganador()

  partida.imprimir_tablero()
