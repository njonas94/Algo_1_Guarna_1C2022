from utiles import *
from interfaz_usuario import *
from validacion import *

import random

def generar_palabra_a_adivinar():
    '''
    Función: generar_palabra_a_adivinar
    Descripción: 
        Selecciona una palabra al azar de las palabras validas.
    Salidas:
        Devuelve la palabra seleccionada en mayúscula.
    '''
    palabras_validas = obtener_palabras_validas()
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

def procesar_intento(palabra_a_adivinar, intento, lista_letras_palabra_a_adivinar):
    '''
    Función: procesar_intento
    Descripción: 
        Compara el intento ingresado con la palabra a adivinar y guarda en una lista el strign del color que corresponde para cada caracter.
    Parametros:
        Palabra_adivinar: Palabra a adivinar en el juego
        Intento: Intento ingresado por el usuario
        Lista_letras_palabra_adivinar: Una lista que contiene las letras de la palabra a adivinar
    Salida:
        Modificamos lista_letras_palabra_adivinar si le pega a la letra y al lugar exacto y lo pintamos de verde
        Nos devuelve una lista con los colores que le pertenecen a cada intento ingresado
    '''
    colores = []
    for pos in range(len(palabra_a_adivinar)):
        if (palabra_a_adivinar.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == palabra_a_adivinar.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == palabra_a_adivinar.index(intento[pos_2]))):
                colores.append(obtener_color('Verde'))
                lista_letras_palabra_a_adivinar[pos] = palabra_a_adivinar[pos]

            elif ((pos == pos_2 and pos_1 == palabra_a_adivinar.index(intento[pos_1])) or (
                    pos == pos_1 and pos_2 == palabra_a_adivinar.index(intento[pos_2]))):
                colores.append(obtener_color('GrisOscuro'))

            elif (pos == pos_1 and pos_1 != palabra_a_adivinar.index(intento[pos_1]) and pos_2 != palabra_a_adivinar.index(intento[pos_1])):
                colores.append(obtener_color('Amarillo'))

            elif (pos == pos_2 and pos_1 != palabra_a_adivinar.index(intento[pos_1]) and pos_2 != palabra_a_adivinar.index(intento[pos_1])):
                colores.append(obtener_color('GrisOscuro'))

        elif intento[pos] not in palabra_a_adivinar:
            colores.append(obtener_color('GrisOscuro'))

        elif intento[pos] in palabra_a_adivinar and intento[pos] != palabra_a_adivinar[pos]:
            colores.append(obtener_color('Amarillo'))

        elif intento[pos] == palabra_a_adivinar[pos]:
            colores.append(obtener_color('Verde'))
            lista_letras_palabra_a_adivinar[pos] = palabra_a_adivinar[pos]

    return colores

def desarrollo_intentos(palabra_a_adivinar, intento, turnos, lista_letras_de_adivinar, lista_letras_de_cada_intento):
    '''
    Función: desarrollo_intentos
    Descripción:
        Orquesta una ronda.
    Parámetros:
        adivinar: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
        todos_turnos: para ir alternando los usuarios.
        Lista_letras_adivinar: Lista que contiene las letras de la pálabra a adivinar.
        Lista_letras_de_cada_intento: Lista de listas con los intentos ingresados separado en letras.
    Salidas:
        Devuelve una lista con las palabras ingresadas.
    '''
    palabras_ingresadas=[]
    while len(palabras_ingresadas)<5 and palabra_a_adivinar not in palabras_ingresadas:
        orden_ingreso=len(palabras_ingresadas)
        #print(lista, palabras_ingresadas, orden_ingreso)
        colores = procesar_intento(palabra_a_adivinar, intento, lista_letras_de_adivinar)
        acumular_intentos(intento, orden_ingreso, colores, lista_letras_de_cada_intento, palabras_ingresadas)

        print('\nPalabra a adivinar: ', end = '')
        mostrar_palabra(lista_letras_de_adivinar)
        for intento in lista_letras_de_cada_intento:
            mostrar_palabra(intento)
            
        if palabra_a_adivinar not in palabras_ingresadas and len(palabras_ingresadas)<5:
            print('Es el turno de:', turnos[len(palabras_ingresadas)].upper())
            arriesgo=input('Arriesgo:')
            intento=validacion_intento_ingresado(arriesgo, palabras_ingresadas)
   
    return palabras_ingresadas

def acumular_intentos(palabra_ingresada, orden_ingreso, colores, lista_letras_de_cada_intento, palabras_ingresadas):
    '''
    Función: acumular_intentos
    Descripción:
        Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.
    Parámetros:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        Contador_intentos: numero que indica el turno
        Colores: lista con los colores correspondientes a la palabra
        Intentos_ingresados_list: Lista de listas con los intentos ingresados por el usuario
        Intentos_ingresados_str: Lista con los intentos en forma de cadenas
    Salidas:
        Acumula los intentos ingresados en una lista de strings
        Modifica la lista de listas con los intentos ingresados con el respectivo color a cada letra

    '''
    palabras_ingresadas.append(palabra_ingresada)
    for i in range(len(palabra_ingresada)):
        lista_letras_de_cada_intento[orden_ingreso][i] = colores[i] + palabra_ingresada[i]

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
        Usuarios: diccionario con los nombres de los jugadores y sus puntajes
    '''
    orden =sorted(jugadores_y_puntos.items(), key=lambda x:x[1], reverse=True)
    if orden[1][1] == orden[0][1]:
        print(f'\nLos jugadores empataron con un total de {orden[1][1]} puntos')
    else:    
        print(f'\nEl ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')
