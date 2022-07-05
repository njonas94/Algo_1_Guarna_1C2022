from utiles import *
from interfaz_usuario import *
from validacion import *

import random

def generar_palabra_a_adivinar(diccionario_palabras_validas):
    '''
    Función: generar_palabra_a_adivinar
    Descripción: 
        Selecciona una palabra al azar de las palabras validas.
    Salidas:
        Devuelve la palabra seleccionada en mayúscula.
    '''
    palabras_validas = list(diccionario_palabras_validas.keys())
    palabra=random.choice(palabras_validas)

    return palabra.upper()

def crear_lista_interrogantes(LONGITUD_PALABRAS):
    '''
    Función: crear_lista_interrogantes
    Descripción: 
        Crea una lista el numero de interrogantes pasado por parametro.
    Parametro:
        LONGITUD_PALABRAS: Recibimos la longitud de las palabras en entero.
    Salida:
        Nos devuelve una lista del tamaño de la longitud pasada por parametro con incognitas adentro.
    '''
    lista_interrogantes = []
    for i in range(LONGITUD_PALABRAS):
        lista_interrogantes.append('?')
    
    return lista_interrogantes

def crear_lista_intentos(CANTIDAD_INTENTOS, lista_interrogantes):
    '''
    Función: crear_lista_intentos
    Descripción:
        Crea una lista con el numero de listas de interrogantes pasado por parametro
    Parametros:
        CANTIDAD_INTENTOS: Nos pasa la cantidad de intentos que va a tener una partida
        Lista_interrogantes: Una lista contenida con interrogantes
    Salida:
        Nos devuelve una lista de listas con la cantidad de intentos que va a tener el juego
    '''
    lista_intentos = []
    for i in range(CANTIDAD_INTENTOS):
        lista_intentos.append(lista_interrogantes.copy())
    
    return lista_intentos

def procesar_intento(palabra_adivinar, intento, lista_letras_palabra_adivinar, longitud_palabras):
    '''
    Función: procesar_intento
    Descripción: 
        Compara el intento ingresado con la palabra a adivinar y guarda en una lista el string del color que corresponde para cada caracter.
    Parametros:
        Palabra_adivinar: cadena de caracteres.
        Intento: cadena de caracteres ingresado por el usuario.
        Lista_letras_palabra_adivinar: Una lista cuyos elementos son caracteres de la palabra a adivinar.
    Salida:
        Modificamos lista_letras_palabra_adivinar si le pega a la letra y al lugar exacto y lo pintamos de verde
        Nos devuelve una lista con los colores que le pertenecen a cada intento ingresado
    '''
    colores = []
    letras_amarillas = {}

    for n in range(longitud_palabras):
        colores.append("")

    for posicion in range(len(intento)):
        if intento[posicion] not in palabra_adivinar:
            colores[posicion] = obtener_color('GrisOscuro')
        elif intento[posicion] == palabra_adivinar[posicion]:
            colores[posicion] = obtener_color('Verde')
            lista_letras_palabra_adivinar[posicion] = palabra_adivinar[posicion]
        elif intento[posicion] in letras_amarillas:
            letras_amarillas[intento[posicion]].append(posicion)
        else:
            letras_amarillas[intento[posicion]] = [posicion]
    
    procesar_letras_amarillas(colores, letras_amarillas, intento, palabra_adivinar)
    

    return colores


def procesar_letras_amarillas(colores, letras_amarillas, intento, palabra_adivinar):
    '''
    Función: procesar_letras_amarillas
    Descripción: 
        Se encarga de asignar color amarillo o gris a las posibles letras amarillas.
    Parametros:
        Palabra_adivinar: cadena de caracteres.
        Intento: cadena de caracteres ingresado por el usuario.
        colores: lista con los colores para asignarle a las letras.
        letras_amarillas: lista con las posibles letras amarillas.
    '''
    for posible_letra_amarilla in letras_amarillas:
        if intento.count(posible_letra_amarilla[0]) <= palabra_adivinar.count(posible_letra_amarilla[0]):
            for i in letras_amarillas[posible_letra_amarilla]:
                colores[i] = obtener_color('Amarillo')
        else:
            indices_gris = intento.count(posible_letra_amarilla[0]) - palabra_adivinar.count(posible_letra_amarilla[0])
            while indices_gris > 0:
                if colores[letras_amarillas[posible_letra_amarilla][-indices_gris]] == "":
                    colores[letras_amarillas[posible_letra_amarilla][-indices_gris]] = obtener_color('GrisOscuro')
                indices_gris -= 1

    for i in range(len(colores)):
        if colores[i] == "":
            colores[i] = obtener_color('Amarillo')


def desarrollo_intentos(palabra_a_adivinar, intento, turnos, lista_letras_palabra_a_adivinar, lista_letras_de_cada_intento, diccionario_palabras_validas, LONGITUD_PALABRAS, CANTIDAD_INTENTOS):
    '''
    Función: desarrollo_intentos
    Descripción:
        Orquesta una ronda.
    Parámetros:
        palabra_a_adivinar: cadena de caracteres.
        intento: cadena de caracteres ingresado por el usuario.
        turnos: orden en que se alternan los usuarios.
        lista_letras_palabra_a_adivinar: Lista que contiene las letras de la pálabra a adivinar.
        Lista_letras_de_cada_intento: Lista de listas con los intentos ingresados separado en letras.
    Salidas:
        Devuelve una lista con las palabras ingresadas.
    '''
    lista_de_intentos_ingresados=[]
    while len(lista_de_intentos_ingresados)<CANTIDAD_INTENTOS and palabra_a_adivinar not in lista_de_intentos_ingresados:
        orden_ingreso = len(lista_de_intentos_ingresados)
        #print(lista, palabras_ingresadas, orden_ingreso)
        colores = procesar_intento(palabra_a_adivinar, intento, lista_letras_palabra_a_adivinar, LONGITUD_PALABRAS)
        acumular_intentos(intento, orden_ingreso, colores, lista_letras_de_cada_intento, lista_de_intentos_ingresados)

        print('\nPalabra a adivinar: ', end = '')
        mostrar_palabra(lista_letras_palabra_a_adivinar)
        for intento in lista_letras_de_cada_intento:
            mostrar_palabra(intento)
            
        if palabra_a_adivinar not in lista_de_intentos_ingresados and len(lista_de_intentos_ingresados)<5:
            print('Es el turno de:', turnos[len(lista_de_intentos_ingresados)].upper())
            intento_sin_validar=input('Arriesgo:')
            intento = validacion_intento_ingresado(intento_sin_validar, lista_de_intentos_ingresados, diccionario_palabras_validas, LONGITUD_PALABRAS)
   
    return lista_de_intentos_ingresados

def acumular_intentos(intento, orden_ingreso, colores, lista_letras_de_cada_intento, lista_de_intentos_ingresados):
    '''
    Función: acumular_intentos
    Descripción:
        Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.
    Parámetros:
        intento: cadena de caracteres ingresado por el usuario.
        orden_ingreso: numero que indica el turno
        Colores: lista con los colores correspondientes a la palabra
        lista_letras_de_cada_intento: Lista de listas con los intentos ingresados por el usuario
        lista_de_intentos_ingresados: Lista con los intentos en forma de cadenas
    Salidas:
        Acumula los intentos ingresados en una lista de strings
        Modifica la lista de listas con los intentos ingresados con el respectivo color a cada letra

    '''
    lista_de_intentos_ingresados.append(intento)
    for i in range(len(intento)):
        lista_letras_de_cada_intento[orden_ingreso][i] = colores[i] + intento[i]

def volver_a_jugar():
    '''
    Función: volver_a_jugar
    Descripción: 
        Pregunta y verifica la respuesta del usuario sobre si quiere volver a jugar o no
    Salida:
        Nos devuelve un string dependiendo si quiere volver a jugar o no del tipo (N.n) o (S,s)
    '''
    desea_jugar = input('\n¿Desea volver a jugar?(S/N):')
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input('¿Desea volver a jugar?(S/N):')
    
    return  desea_jugar

def determinar_ganador(jugadores_y_puntos):
    '''
    Funcion: determinar_ganador
    Descripción:
        Ordena el diccionario en una lista y los compara para ver si hay un ganador o no
    Parametros:
        jugadores_y_puntos: diccionario con los nombres de los jugadores y sus puntajes
    '''
    orden =sorted(jugadores_y_puntos.items(), key=lambda x:x[1], reverse=True)
    if orden[1][1] == orden[0][1]:
        print(f'\nLos jugadores empataron con un total de {orden[1][1]} puntos')
    else:    
        print(f'\nEl ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')
