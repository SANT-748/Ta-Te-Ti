import os
import time

global estado_juego

if os.name == "nt":
    type="cls"

def clear(type):
    os.system(type)

tablero=[" ", " ", " ",
         " ", " ", " ",
         " ", " ", " ",]

def inicializar_tablero(tablero):
    for i in range(9):
        tablero[i]= " "

def imprimir_tablero(tablero):
    print(" ",tablero[6],"|",tablero[7],"|",tablero[8],"                   7 | 8 | 9")                         
    print(" ___|___|___                  ___|___|___")
    print(" ",tablero[3],"|",tablero[4],"|",tablero[5],"                   4 | 5 | 6")
    print(" ___|___|___                  ___|___|___")
    print(" ",tablero[0],"|",tablero[1],"|",tablero[2],"                   1 | 2 | 3")
    print("    |   |                        |   |   ")

def informacion_tablero(tablero,num_jugador):
    clear(type)
    print(f"Turno del jugador {num_jugador}:\n")
    imprimir_tablero(tablero)

def agregar_casilla(tablero,marca_jugador,num_jugador):
    casilla=int(input("\nIngrese una casilla (1 al 9): "))
    while (casilla < 1 or casilla > 9 or tablero[casilla-1] != " "):
        informacion_tablero(tablero,num_jugador)
        print("Error, casilla invalida")
        casilla=int(input("Ingrese una casilla (1 al 9): "))
        
    tablero[casilla-1]=marca_jugador

def verificar_estado_juego(tablero,turno):
    if turno == 9:
        return "empate"
    elif tablero[0] != " " and tablero[0] == tablero[4] and tablero[0] == tablero[8]:       #Ver si en el tablero la diagonal de izquierda a derecha tiene 3 marcas iguales (para fin del juego)
        return False
    elif tablero[2] != " " and tablero[2]== tablero[4] and tablero[2] == tablero[6]:       #Ver si en el tablero la diagonal de derecha a izquierda tiene 3 marcas iguales (para fin del juego)
        return False
    else:
        for i in range (0,7,3):      #En rango de 0 a 6 con paso 3
            if tablero[i] != " ":    #Ver unicamente si la casilla tiene alguna marca
                if tablero[i] == tablero[i+1] and tablero[i] == tablero[i+2]:     #Ver si en el tablero hay alguna fila con 3 marcas iguales (para fin del juego)
                    return False
        
        for i in range (3):
            if tablero[i] != " ":    #Ver unicamente si la casilla tiene alguna marca
                if tablero[i] == tablero[i+3] and tablero[i] == tablero[i+6]:   #Ver si en el tablero hay alguna columna con 3 marcas iguales (para fin del juego)
                    return False
    return True
        
def estado_TaTeTi():
    respuesta_juego=""
    respuesta_juego=(str(input("Desea volver a jugar? (s/n):"))).lower()
    while respuesta_juego.lower() != "s" and respuesta_juego.lower() != "n":
        clear(type)
        print('Error, ingrese "s" para volver a jugar o "n" para finalizar el programa')
        respuesta_juego=(str(input("Desea volver a jugar? (s/n):")).lower())
    return respuesta_juego

def juego():
    volver_jugar="s"
    while (volver_jugar.lower() == "s"):

        estado_juego=True
        num_jugador=1
        marca_jugador="X"
        turno=1
        inicializar_tablero(tablero)

        while (estado_juego == True):
            
            clear(type) #Limpiar pantalla

            if turno != 1:
                if num_jugador == 1:
                    num_jugador = 2
                    marca_jugador="O"
                elif num_jugador == 2:
                    num_jugador = 1
                    marca_jugador="X"

            informacion_tablero(tablero,num_jugador)
        
            agregar_casilla(tablero,marca_jugador,num_jugador)
            
            informacion_tablero(tablero,num_jugador)

            time.sleep(0.5)

            if turno >= 3:
                estado_juego=verificar_estado_juego(tablero,turno)      #Verificar si el juego continua

            turno=turno+1

        if estado_juego != "empate":
            clear(type)
            print("Felicitaciones !!")
            print(f'El jugador numero {num_jugador} con la marca "{marca_jugador}" Gano el juego !! \n')
            imprimir_tablero(tablero)
        else:
            clear(type)
            print("El juego termino en empate\n")
            imprimir_tablero(tablero)
        time.sleep(2)
        volver_jugar=estado_TaTeTi()  #Preguntar si desea seguir jugando y ese valor asignarlo a volver_jugar

    clear(type)
    print("Gracias por jugar !! :D\n")
    time.sleep(1.5)



juego()



