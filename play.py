#play.py
#Created by Pedro Santiago Salazar
#Run this file to play

import mineslib as ml

print("         ### BIENVENIDO A BUSCAMINAS_PY ###")
print("      'Es mas facil leer su codigo que ganarlo'\n")
tipo = ""
rows, cols = 0, 0
board = []

#while the user does not exit the game
while tipo!="S":

    tipo = ml.menu()
    
    #if the player decides to play
    if tipo!="L" and tipo!="H" and tipo!="S":
        
        #set the game mode and board
        rows, cols, numbombs = ml.modo(tipo)
        print("Tamano del board:",str(rows)+"x"+str(cols))
        print("# Bombas:",numbombs)

        #Starts the game
        print("Inicia el juego:\n")
        board, bombs = ml.newgame(rows, cols, numbombs)
        turn = rows*cols-len(bombs)
        
        #while the game does not end
        while(True):
            print("***Empieza el turno\nTablero:")
            ml.draw(board)
            print("Bombas:",len(bombs)," Turnos para ganar:",turn)
            
            #if player wins
            if turn==0:
                print("Has ganado! Felicidades")
                break
            tf, tc, flag = ml.selec(rows,cols)
            
            #if player decides to put a flag on a cell
            if flag:
                if not board[tf][tc].isnumeric():
                    board[tf][tc] = "?"
                    continue
            
            #if player hits a bombs (therefore loses the game)
            elif [tf,tc] in bombs:
                for coor in bombs:
                    if board[coor[0]][coor[1]] == "?":
                        board[coor[0]][coor[1]] = "!"
                    else:
                        board[coor[0]][coor[1]] = "X"
                board[tf][tc] = "+"
                print("\nTablero:")
                ml.draw(board)
                print("Has perdido! Mejor suerte para la proxima")
                break
            
            #else the cell gets uncovered
            else:
                if not board[tf][tc].isnumeric():
                    turn -= 1
                    board[tf][tc] = str(ml.buscaminas(rows,cols,tf,tc,bombs))              

        #Game over
        print("\nFin del juego\n")
        a = input("Presiona ENTER para continuar...")

    #if player chooses the symbols' meaning option
    elif tipo=="L":
        ml.printleg()
        
    #if player chooses help option
    elif tipo=="H":
        ml.printhelp()
        
print("Gracias por jugar a Buscaminas_PY. Vuelve pronto!")
