import random

def puntaje(lista_intentos, palabra_adivinar, jugadores_y_puntos, orden_turnos):
    '''
    Función: puntaje
    Parámetros:
        lista_intentos: lista cargada con cadenas de caracteres.
        palabra_adivinar: cadena de caracteres.
        jugadores_y_puntos: diccionario cargado.
        orden_turnos: lista cargada.
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
    '''
    valores=[50,40,30,20,10,-50,-100]
    if palabra_adivinar not in lista_intentos and len(lista_intentos)==5:
        jugadores_y_puntos[orden_turnos[0]]+= valores[-1]
        jugadores_y_puntos[orden_turnos[1]]+= valores[-2]
        print(f"{orden_turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {jugadores_y_puntos[orden_turnos[0]]} puntos.")
        print(f"{orden_turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {jugadores_y_puntos[orden_turnos[1]]} puntos.")
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
        jugadores_y_puntos = contador_puntajes (puntos_obtenidos, jugadores_y_puntos, orden_turnos, indice)
    
    return jugadores_y_puntos

def contador_puntajes (puntos_obtenidos, usuarios, turnos, indice):
    ''' 
    Funcion que acumula el puntaje para cada jugador.
    '''
    jugador_acierto = turnos[indice]
    if indice ==0:
        jugador_fallo = turnos[indice-2]
    else:
        jugador_fallo = turnos[indice-1]
    usuarios[jugador_acierto] += puntos_obtenidos
    if puntos_obtenidos > 0:
        usuarios[jugador_fallo] += -puntos_obtenidos
        print(f"{jugador_acierto.upper()}, ha ganado: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_acierto]} puntos.")
        print(f"{jugador_fallo.upper()}, ha perdido: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_fallo]} puntos.")
    
    return usuarios

def orden_turnos (usuarios):
    ''' 
    Generador de turnos 
    '''
    turnos = []
    jugadores = list(usuarios.keys())
    master=random.choice(jugadores)
    indice = jugadores.index(master)
    for i in range(5):
        if i in (0,2,4):
            turnos.append(master)              
        else:
            turnos.append(jugadores[indice-1])
    
    return turnos