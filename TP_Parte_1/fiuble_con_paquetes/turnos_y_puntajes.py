import random

def puntaje(lista_intentos, palabra_adivinar, jugadores_y_puntos, turnos):
    '''
    Función: puntaje
    Descripción:
    Parámetros:
        lista_intentos: lista de strings con los intentos ingresados
        palabra_adivinar: palabra a adivinar en el juego
        jugadores_y_puntos: diccionario con los jugadores y sus puntajes
        turnos: lista con los turnos
    Salidas:
        Devuelve el diccionario de los jugadores cargado con el puntaje obtenido una vez finalizada la partida.
        Imprime en caso de que los jugadores no hallan adivinado la palabra.
    '''
    valores=[50,40,30,20,10,-50,-100]
    if palabra_adivinar not in lista_intentos and len(lista_intentos)==5:
        jugadores_y_puntos[turnos[0]]+= valores[-1]
        jugadores_y_puntos[turnos[1]]+= valores[-2]
        print(f'{turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {jugadores_y_puntos[turnos[0]]} puntos.')
        print(f'{turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {jugadores_y_puntos[turnos[1]]} puntos.')
    elif palabra_adivinar in lista_intentos:
        if len(lista_intentos)==1:
            puntos_obtenidos=valores[0]
        elif len(lista_intentos)==2:
            puntos_obtenidos=valores[1]
        elif len(lista_intentos)==3:
            puntos_obtenidos=valores[2]
        elif len(lista_intentos)==4:
            puntos_obtenidos=valores[3]
        elif len(lista_intentos)==5:
            puntos_obtenidos=valores[4]
        indice = len(lista_intentos)-1
        jugadores_y_puntos = contador_puntajes (puntos_obtenidos, jugadores_y_puntos, turnos, indice)
    
    return jugadores_y_puntos

def contador_puntajes (puntos_obtenidos, jugadores_y_puntos, turnos, indice):
    '''
    Funcion: contador_puntajes
    Descripción:
        Muestra y acumula los puntajes obtenidos en cada ronda
    Parametros:
        Puntos_obtenidos: Puntos obtenidos al terminar cada ronda
        jugadores_y_puntos: diccionario con los jugadores y sus respectivos puntos acumulados
        Turnos: lista con los turnos
        Indice:
    Salida:
        Nos devuelve el diccionario de jugadores modificado por el puntaje obtenido
    '''
    jugador_acierto = turnos[indice]
    if indice ==0:
        jugador_fallo = turnos[indice-2]
    else:
        jugador_fallo = turnos[indice-1]
    jugadores_y_puntos[jugador_acierto] += puntos_obtenidos
    if puntos_obtenidos > 0:
        jugadores_y_puntos[jugador_fallo] += -puntos_obtenidos
        print(f'{jugador_acierto.upper()}, ha ganado: {puntos_obtenidos} puntos. Tiene acumulados {jugadores_y_puntos[jugador_acierto]} puntos.')
        print(f'{jugador_fallo.upper()}, ha perdido: {puntos_obtenidos} puntos. Tiene acumulados {jugadores_y_puntos[jugador_fallo]} puntos.')
    
    return jugadores_y_puntos

def orden_turnos (jugadores_y_puntos):
    '''
    Funcion: orden_turnos
    Descripción:

    Parametros:
        jugadores_y_puntos: diccionario con los jugadores y sus puntajes
    Salida:
        Nos retorna una lista con los respectivos turnos para el juego
    '''
    turnos = []
    jugadores = list(jugadores_y_puntos.keys())
    master=random.choice(jugadores)
    indice = jugadores.index(master)
    for i in range(5):
        if i in (0,2,4):
            turnos.append(master)              
        else:
            turnos.append(jugadores[indice-1])
    
    return turnos

def cambio_turnos (turnos):
    '''
    Función: cambio_turnos
    Descripción: 
    Parametros:
        turnos: Lista con los turnos de los jugadores
    Salida:
        Nos retorna la lista de turnos reordenada
    '''
    turnos.append(turnos[1])
    del(turnos[0])
    
    return turnos
