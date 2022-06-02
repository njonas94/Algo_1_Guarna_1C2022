import random

def puntaje(lista_de_intentos_ingresados, palabra_adivinar, jugadores_y_puntos, turnos):
    '''
    Función: puntaje
    Descripción:
        Asigna el puntaje correspondiente y lo carga en el diccionario de jugadores y puntos.
    Parámetros:
        lista_de_intentos_ingresados: Lista de strings con los intentos ingresados.
        palabra_adivinar: Palabra a adivinar en el juego.
        jugadores_y_puntos: Diccionario con los jugadores y sus puntajes.
        turnos: Lista con los turnos.
    Salidas:
        Devuelve el diccionario de los jugadores cargado con el puntaje obtenido una vez finalizada la partida.
        Imprime en caso de que los jugadores no hallan adivinado la palabra.
    '''
    valores=[50,40,30,20,10,-50,-100]
    if palabra_adivinar not in lista_de_intentos_ingresados and len(lista_de_intentos_ingresados)==5:
        jugadores_y_puntos[turnos[0]]+= valores[-1]
        jugadores_y_puntos[turnos[1]]+= valores[-2]
        print(f'{turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {jugadores_y_puntos[turnos[0]]} puntos.')
        print(f'{turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {jugadores_y_puntos[turnos[1]]} puntos.')
    elif palabra_adivinar in lista_de_intentos_ingresados:
        if len(lista_de_intentos_ingresados)==1:
            puntos_obtenidos=valores[0]
        elif len(lista_de_intentos_ingresados)==2:
            puntos_obtenidos=valores[1]
        elif len(lista_de_intentos_ingresados)==3:
            puntos_obtenidos=valores[2]
        elif len(lista_de_intentos_ingresados)==4:
            puntos_obtenidos=valores[3]
        elif len(lista_de_intentos_ingresados)==5:
            puntos_obtenidos=valores[4]
        indice = len(lista_de_intentos_ingresados)-1
        jugadores_y_puntos = contador_puntajes (puntos_obtenidos, jugadores_y_puntos, turnos, indice)
    
    return jugadores_y_puntos

def contador_puntajes (puntos_obtenidos, jugadores_y_puntos, turnos, indice):
    '''
    Funcion: contador_puntajes
    Descripción:
        Muestra y acumula los puntajes obtenidos en cada ronda.
    Parametros:
        Puntos_obtenidos: Numero entero, representa el puntaje al terminar la ronda.
        jugadores_y_puntos: Diccionario con los jugadores y sus respectivos puntos acumulados.
        Turnos: Lista con los turnos.
        Indice: Entero que se utiliza como indice para acceder a la lista turnos.
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

def orden_turnos (jugadores_y_puntos, CANTIDAD_INTENTOS):
    '''
    Funcion: orden_turnos
    Descripción:
        Asigna el orden de los turnos de los jugadores.
    Parametros:
        jugadores_y_puntos: diccionario con los jugadores y sus puntajes.
        CANTIDAD_INTENTOS: Nos pasa la cantidad de intentos que va a tener una partida.
    Salida:
        Nos retorna una lista con los respectivos turnos para el juego.
    '''
    turnos = []
    jugadores = list(jugadores_y_puntos.keys())
    master = random.choice(jugadores)
    indice = jugadores.index(master)
    for i in range(CANTIDAD_INTENTOS):
        if i % 2 == 0:
            turnos.append(master)              
        else:
            turnos.append(jugadores[indice-1])
    
    return turnos

def cambio_turnos (turnos):
    '''
    Función: cambio_turnos
    Descripción:
        Alterna el turno entre los jugadores.
    Parametros:
        turnos: Lista con los turnos de los jugadores
    Salida:
        Nos retorna la lista de turnos reordenada
    '''
    turnos.append(turnos[1])
    del(turnos[0])
    
    return turnos
