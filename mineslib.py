#mineslib.py
#Created by Pedro Santiago Salazar

from random import randint as rnd

#function that counts how many bombs are around a cell
def buscaminas(rows, cols, i, j, bombs):
  num = 0
  # (i-1, j-1) (i-1, j) (i-1, j+1)
  #  (i, j-1)   (i, j)   (i,j+1)
  # (i+1, j-1) (i+1, j) (i+1, j+1)
  for f in range(i-1, i+2):
    for c in range(j-1, j+2):  
      if c >= 0 and c < cols and f >= 0 and f < rows:
        if not(f==i and c==j):
          if [f,c] in bombs:
            num += 1
  return num

#function that draws the board
def draw(board):
    lim = len(board[0])*2+2
    for j in range(lim//2+1):
        if j==0 or j==lim//2:
            print(".", end=" ")
        else:
            print(j-1, end=" ")
    print()
    for j in range(lim+1):
        print("=", end="")
    print()
    ix = 0
    for r in board:
        print("| ", end="")
        for c in r:
            print(c, end=" ")
        print("|",ix)
        ix += 1
    for j in range(lim+1):
        print("=", end="")
    print()

#function that shows the menu and reads the player's option
def menu():
    resp = ""
    opcs = ["I","M","D","P","L","H","S"]
    print("      Seleccionar una opcion (letra entre los parentesis):")
    print("MODOS DE JUEGO")
    print("  1. Iniciante............................ (I)")
    print("  2. Intermedio........................... (M)")
    print("  3. Dificil.............................. (D)")
    print("  4. Personalizado........................ (P)")
    print("OTRAS OPCIONES")
    print("  5. Que son los simbolos en el tablero?.. (L)")
    print("  6. Ayuda................................ (H)")
    print("  7. Salir del juego...................... (S)")
    while resp not in opcs:
        resp = input("\nSeleccionar ahora (I, M, D, P, L, H, S): ")
        resp = resp.upper()
    return resp

#function that returns the game parameters (#rows, #colmuns, #bombs) according to the player's choice
def modo(resp):
    f, c, b = 0, 0, 0
    if resp=="I":
        f, c, b = 4, 4, 4
    elif resp=="M":
        f, c, b = 6, 6, 11
    elif resp=="D":
        f, c, b = 8, 8, 20
    elif resp=="P":
        while f < 3 or f > 12:
            aux = input("Elegir el tamano del tablero. Numero de filas (Entre 3 y 12): ")
            if aux.isnumeric():
              f = int(aux)
        while c < 3 or c > 12:
            a2 = input("Ahora el numero de columnas (Entre 3 y 12): ")
            if a2.isnumeric():
              c = int(a2)
        b = ( (f*c)//4 ) + 1
    else:
      print("Error en mineslib.modo(resp): ocurrio un error en la eleccion del modo de juego")
    return (f, c, b)

#create board (tabl) and set the positions of all the bombs (saving them in bombs list)
def newgame(f, c, b):
    tabl = []
    bombs = []
    for i in range(f):
        rowx = []
        for j in range(c):
            rowx.append("#")
        tabl.append(rowx)
    while b!=0:
        ri, rj = -1, -1
        while ri<0 or [ri,rj] in bombs:
            ri, rj = rnd(0,f-1), rnd(0,c-1)
        bombs.append([ri,rj])
        b -= 1
    bombs.sort()
    return (tabl, bombs)  

#print help
def printhelp():
    print("\nNecesitas ayuda?")
    print("  1. Sobre el menu\n  2. Sobre el tablero\n  3. Sobre el juego\n  4. Sobre las banderas")
    print("\n1. SOBRE EL MENU")
    print("  * Cuanto te aparezca el menu principal, ingresa la letra de acuerdo a la opcion que elijas:")
    print("     'I' para jugar en modo iniciante (tablero 4x4, numero de bombas: 4)")
    print("     'M' para jugar en modo intermedio (tablero 6x6, numero de bombas: 11)")
    print("     'D' para jugar en modo dificil (tablero 8x8, numero de bombas: 20)")
    print("     'P' para jugar en modo personalizado (tamano del tablero elegido por el usuario,")
    print("                                           numero de bombas calculado automaticamente,")
    print("                                           tamano min: 3x3, tamano max: 12x12)")
    print("     'L' para conocer cada uno de los simbolos que aparecern en el tablero")
    print("     'H' para ingresar a esta ayuda")
    print("     'S' para salir del juego")
    a = input("\nPresiona ENTER para continuar a: 2. Sobre el tablero")
    print("\n2. SOBRE EL TABLERO")
    print("  * Los numeros sobre el tablero indican la columna de cada celda")
    print("  * Los numeros a la derecha del tablero indica la fila de cada celda")
    print("  * Ten en cuenta estos numeros cuando te pidan elegir la fila y la columna")
    print("  * Ejemplo: La primera celda del tablero es              fila 0 columna 0 (0, 0)")
    print("             La celda abajo de ella es                    fila 1 columna 0 (1, 0)")
    print("             La celda a la derecha de la primera celda es fila 0 columna 1 (0, 1)")
    a = input("\nPresiona ENTER para continuar a: 3. Sobre el juego")
    print("\n3. SOBRE EL JUEGO")
    print("  * El objetivo es descubrir todos los espacios del tablero sin bombas")
    print("  * GANAS   cuando descubres todos los espacios sin bomba, sin chocar con ninguna bomba")
    print("  * PIERDES cuando descubres un espacio con bomba")
    print("  * Cuando se te pida ingresar la fila, ingresa el numero de fila y presiona ENTER")
    print("  * Cuando se te pida ingresar la columna, ingresa el numero de columna y presiona ENTER")
    print("  * Puedes usar banderas (su simbolo es '?') para ayudarte en el juego")
    a = input("\nPresiona ENTER para continuar a: 4. Sobre las banderas")
    print("\n4. SOBRE LAS BANDERAS")
    print("  * Si sospechas que una celda tiene una bomba, puedes indicar esa celda con una bandera (simbolo: ?)")
    print("  * Usar una bandera te ayuda visualmente durante el juego")
    print("  * Usar banderas es opcional, no las uses hasta que te sientas comodo/a con ellas")
    print("  * Como dibujarlas?")
    print("    > Cuando se te pida ingresar la fila de la celda que deseas descubrir,")
    print("      ingresa el numero de la fila JUNTO al simbolo ! (sin espacios entre el numero y el simbolo)")
    print("    > Ejemplos: ///  Fila: 2!  -> correcto ///  Fila: 2 !  -> incorrecto ///")
    print("    > A continuacion, presionas ENTER y se te pedira ingresar el numero de columna")
    print("    > Ingresa el numero de columna normalmente")
    print("    > Si quieres descubrir una casilla con bandera, solo ingresa su numero de fila y columna normalmente")
    print("\nDisfruta del juego :)")
    a = input("\nPresiona ENTER para continuar...")
    print()

#print the meaning of the symbols printed on the board throughout the game
def printleg():
    print("\nQue significan los simbolos en el tablero?\n")
    print("  *Durante el juego\n")
    print("  #:      celda no descubierta")
    print("  numero: celda descubierta, indica el numero de bombas alrededor de la celda")
    print("  ?:      celda que pusiste una bandera, puede o no tener una bomba\n")
    print("  *Cuando termina el juego\n")
    print("  +:      celda elegida pero con bomba, SI chocaste contra esa bomba")
    print("  X:      celda no elegida con bomba,   NO chocaste contra esa bomba")   
    print("  !:      celda que pusiste una bandera, y SI tenia una bomba")
    print("\nDisfruta del juego :)")
    a = input("Presiona ENTER para continuar...")
    print()

#read the player's input for the row number, column number and whether a flag must be put
def selec(rows,cols):
    print("Selecciona una ubicacion Fila 0-"+str(rows-1),"Columna 0-"+str(cols-1))
    tf, tc, flag = -1, -1, False
    while tf < 0 or tf > rows-1:
        aux = input("Fila:")
        if len(aux)>0 and aux[-1] == "!":
          flag = True
          aux = aux[:-1]
        if aux.isnumeric():
          tf = int(aux)
        else:
          flag = False
    while tc < 0 or tc > cols-1:
        a2 = input("Columna:")
        if a2.isnumeric():
          tc = int(a2)
    print()
    return (tf, tc, flag)
