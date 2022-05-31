import random

def puntaje(lista,adivinar,usuarios,turnos):
    '''
    Función: puntaje
    Parámetros:
        lista: lista de cadenas de caracteres.
        adivinar: cadena de caracteres, palabra a adivinar.
        todos_turnos: lista vacia.
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
    '''
    valores=[50,40,30,20,10,-50,-100]
    if adivinar not in lista and len(lista)==5:
        usuarios[turnos[0]]+= valores[-1]
        usuarios[turnos[1]]+= valores[-2]
        print(f"{turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {usuarios[turnos[0]]} puntos.")
        print(f"{turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {usuarios[turnos[1]]} puntos.")
    elif adivinar in lista:
        if len(lista)==1:
            puntos_obtenidos=valores[0]
        elif len(lista)==2:
            puntos_obtenidos=valores[1]
        elif len(lista)==3:
            puntos_obtenidos=valores[2]
        elif len(lista)==4:
            puntos_obtenidos=valores[3]
        elif len(lista)==5:
            puntos_obtenidos=valores[4]
        indice = len(lista)-1
        usuarios = contador_puntajes (puntos_obtenidos,usuarios,turnos,indice)
    
    return usuarios

def contador_puntajes (puntos_obtenidos,usuarios,turnos,indice):
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
    nombre = list(usuarios.keys())
    master=random.choice(nombre)
    indice = nombre.index(master)
    for i in range(5):
        if i in (0,2,4):
            turnos.append(master)              
        else:
            turnos.append(nombre[indice-1])
    
    return turnos