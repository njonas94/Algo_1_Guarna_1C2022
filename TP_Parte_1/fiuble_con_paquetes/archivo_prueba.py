from interfaz_usuario import *
from jugabilidad import *
from turnos_y_puntajes import *
from validacion import *

import random
import time
import doctest

#Validacion

def cambiar_tilde(palabra_ingresada):
    '''    
    >>> cambiar_tilde('âbrîa')
    'abria'
    >>> cambiar_tilde('àctúo')
    'actuo'
    >>> cambiar_tilde('pingüinò')
    'pinguino'
    >>> cambiar_tilde('sòl')
    'sol'
    '''
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = palabra_ingresada.maketrans(a, b)
    arriesgo = palabra_ingresada.translate(palabra_sin_acento)

    return arriesgo
print(doctest.testmod())

def no_es_alfabetico (palabra_ingresada):
    """
    >>> no_es_alfabetico('perro0')
    True
    >>> no_es_alfabetico('$APO')
    True
    >>> no_es_alfabetico('fisura')
    False
    >>> no_es_alfabetico('HELADOS')
    False
    >>> no_es_alfabetico('&contraseña_123&')
    True
    """
    return not palabra_ingresada.isalpha()
print(doctest.testmod())

def longitud_palabra (palabra_ingresada):
    """
    >>> longitud_palabra('algoritmos')
    True
    >>> longitud_palabra('pajar')
    False
    >>> longitud_palabra('ACTUO')
    False
    >>> longitud_palabra('hola')
    True
    >>> longitud_palabra('333333')
    True
    >>> longitud_palabra('')
    True
    """
    return len(palabra_ingresada)!= 5
print(doctest.testmod())

def validar_palabra (palabra_ingresada):
    """
    >>> validar_palabra ('manco')
    False
    >>> validar_palabra ('parda')
    False
    >>> validar_palabra ('mouse')
    True
    >>> validar_palabra ('budin')
    True
    """
    return not no_es_alfabetico (palabra_ingresada) and palabra_ingresada not in palabras_validas()
print(doctest.testmod())

def validar_ingreso (palabra_ingresada, intentos_ingresados_str):
    """
    >>> validar_ingreso ('pesas', 'panes')
    False
    >>> validar_ingreso ('rosas', 'rimar')
    False
    >>> validar_ingreso ('MANCO', 'MANCO')
    True
    >>> validar_ingreso ('PARDA', 'PARDA')
    True
    """
    return palabra_ingresada.upper() in intentos_ingresados_str
print(doctest.testmod())

def longitud_y_alfabetica(palabra_ingresada):
    """
    >>> longitud_y_alfabetica('pican')
    False
    >>> longitud_y_alfabetica('hola')
    False
    >>> longitud_y_alfabetica('contraseña')
    False
    >>> longitud_y_alfabetica('contraseña123')
    True
    >>> longitud_y_alfabetica('h0la')
    True
    """
    return not palabra_ingresada.isalpha() and len(palabra_ingresada) != 5
print(doctest.testmod())

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
def validacion_intento_ingresado(palabra_ingresada, lista_palabras_ingresadas):
    '''
    Función: validar_intento_ingresado
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        lista_palabras_ingresadas: lista de cadenas de caracteres.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    while no_es_alfabetico (palabra_ingresada) or validar_palabra (palabra_ingresada) or validar_ingreso (palabra_ingresada, lista_palabras_ingresadas):

        if longitud_y_alfabetica(palabra_ingresada):
            print("Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.")

        elif no_es_alfabetico (palabra_ingresada):
            print("La palabra no tiene que contener numero ni caracteres especiales.")

        elif longitud_palabra (palabra_ingresada): 
            print("La palabra tiene que ser de 5 letras.")

        elif validar_ingreso (palabra_ingresada, lista_palabras_ingresadas):
            print("La palabra ya habia sido ingresada.")

        elif validar_palabra (palabra_ingresada):
            print("La palabra no se encuentra en la lista de palabras válidas.")

        palabra_ingresada = input("Ingrese una palabra valida de 5 letras: ")
        palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())

    return palabra_ingresada.upper()
print(doctest.testmod())

#---------------------------------------------------------------------------------------------------

#Turno y Puntajes

def puntaje(lista_intentos, palabra_adivinar, jugadores_y_puntos, orden_turnos):
    '''
    Función: puntaje
    Parámetros:
        lista_intentos: lista de strings con los intentos ingresados
        palabra_adivinar: palabra a adivinar en el juego
        jugadores_y_puntos: diccionario con los jugadores y sus puntajes
        orden_turnos: lista con los turnos
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
        
    >>> puntaje(["bardo","copas","hojas"], "hojas", {"nico":0, "pepito":0}, ["nico","pepito","nico","pepito","nico"])
    NICO, ha ganado: 30 puntos. Tiene acumulados 30 puntos.
    PEPITO, ha perdido: 30 puntos. Tiene acumulados -30 puntos.
    {'nico': 30, 'pepito': -30}
    >>> puntaje(["leche","matar","mazos","muros","malos"], "malos", {"seba":0, "juan":0}, ["juan","seba","juan","seba","juan"])
    JUAN, ha ganado: 10 puntos. Tiene acumulados 10 puntos.
    SEBA, ha perdido: 10 puntos. Tiene acumulados -10 puntos.
    {'seba': -10, 'juan': 10}
    >>> puntaje(["dunas"], "dunas", {"luis":0, "carla":0}, ["luis","carla","luis","carla","luis"])
    LUIS, ha ganado: 50 puntos. Tiene acumulados 50 puntos.
    CARLA, ha perdido: 50 puntos. Tiene acumulados -50 puntos.
    {'luis': 50, 'carla': -50}
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
print(doctest.testmod())

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
    >>> orden_turnos ({'brian':0,'martin':0}, 5)
    ['brian', 'martin', 'brian', 'martin', 'brian']
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
print(doctest.testmod())

def cambio_turnos (turnos):
    '''
    Función: cambio_turnos
    Descripción:
        Alterna el turno entre los jugadores.
    Parametros:
        turnos: Lista con los turnos de los jugadores
    Salida:
        Nos retorna la lista de turnos reordenada
    >>> cambio_turnos (['nico', 'pepito', 'nico', 'pepito', 'nico'])
    ['pepito', 'nico', 'pepito', 'nico', 'pepito']
    >>> cambio_turnos (['juan','seba','juan','seba','juan'])
    ['seba', 'juan', 'seba', 'juan', 'seba']
    '''
    turnos.append(turnos[1])
    del(turnos[0])
    
    return turnos
print(doctest.testmod())

#---------------------------------------------------------------------------------------------

#interfaz_usuario

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
def mostrar_palabra(palabra_ingresada):
    '''
    Función: mostrar_palabra
    Descripción: 
        Recibe una palabra y la muestra en el formato deseado.
    Parametro:
        palabra_ingresada: Palabra que segun el momento de su ejecución varía.
    '''
    for letra in palabra_ingresada:
        print(letra + ' ' + obtener_color('Defecto'), end = '')
    print()
print(doctest.testmod())

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
def ingreso_jugadores():
    '''
    Función: ingreso_jugadores
    Descripción: 
        Crea un diccionario con los nombres como claves y de valor sus puntajes.  
    Salidas:
        Nos retorna el diccionario.
    '''
    jugadores_y_puntos = {}
    jugador_1 = input('Ingrese el nombre del 1er usuario:').upper()
    jugador_2 = input('Ingrese el nombre del 2do usuario:').upper()
    while jugador_1 == jugador_2:
        print(f'Nombre "{jugador_1}" no disponible. Ingrese un nombre distinto.')
        jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()   
    
    jugadores_y_puntos[jugador_1] = 0
    jugadores_y_puntos[jugador_2] = 0

    return jugadores_y_puntos

#--------------------------------------------------------------------------------------------------------------

#jugabilidad

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
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

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
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

#Devido a la complejidad del retorno de la funcion no se pudo realizar el Doctest
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
    return palabras_ingresadas,lista_letras_de_cada_intento
palabras_ingresadas,lista_letras_de_cada_intento=acumular_intentos('MOROS', 2, ['\x1b[32m','\x1b[39m','\x1b[32m','\x1b[39m','\x1b[32m'], [['O','N','Z','A','S'],['O','P','E','R','A'],['?','?','?','?','?'],['?','?','?','?','?'],['?','?','?','?','?']], ['ONZAS','OPERA'])
    
def determinar_ganador(jugadores_y_puntos):
    '''
    Funcion: determinar_ganador
    Descripción:
        Ordena el diccionario en una lista y los compara para ver si hay un ganador o no
    Parametros:
        jugadores_y_puntos: diccionario con los nombres de los jugadores y sus puntajes
    >>> determinar_ganador({"nico":-30, "pepito":30})
    El ganador es PEPITO con un total de 30 puntos.
    >>> determinar_ganador({"nico":30, "pepito":-30})
    El ganador es NICO con un total de 30 puntos.
    >>> determinar_ganador({"nico":30, "pepito":30})
    Los jugadores empataron con un total de 30 puntos
    '''
    orden =sorted(jugadores_y_puntos.items(), key=lambda x:x[1], reverse=True)
    if orden[1][1] == orden[0][1]:
        print(f'Los jugadores empataron con un total de {orden[1][1]} puntos')
    else:    
        print(f'El ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')
print(doctest.testmod())
