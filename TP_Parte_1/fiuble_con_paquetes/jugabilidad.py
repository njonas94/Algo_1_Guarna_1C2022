from utiles import *
from interfaz_usuario import *
from validacion import *

import random

def generar_palabra_a_adivinar():
    '''
    Función: generar_palabra_a_adivinar
        Devuelve la palabra a adivinar en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.
    Salidas:
        Devuelve la palabra seleccionada aleatoriamente en mayúscula.
    '''
    palabras_validas = obtener_palabras_validas()
    palabra=random.choice(palabras_validas)

    return palabra.upper()

def crear_lista_interrogantes(LONGITUD_PALABRAS):
    '''
    Autor : Aldair Torres
    Pre: recibe la palabra a adivinar para saber su longitud
    Post: Nos devuelve una lista conformada por signos de interrogacion
    '''
    lista_interrogantes = []
    for i in range(LONGITUD_PALABRAS):
        lista_interrogantes.append('?')
    
    return lista_interrogantes

def crear_lista_intentos(CANTIDAD_INTENTOS, lista_interrogantes):
    '''
    Autor: Aldair Torres
    Pre: recibe una cantidad de intentos y una lista con interrogantes
    Post: Nos devuelve una lista de listas en donde se almacenas los intentos
    '''
    lista_intentos = []
    for i in range(CANTIDAD_INTENTOS):
        lista_intentos.append(lista_interrogantes.copy())
    
    return lista_intentos

def procesar_intento(pal_adiv, intento, lista_palabra_a_adivinar):
    '''
    Procesa el intento ingresado, creando una lista con el correspondiente color asignado a cada letra en el mismo indice que el string ingresado.
    '''
    colores = []
    for pos in range(len(pal_adiv)):
        if (pal_adiv.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == pal_adiv.index(intento[pos_2]))):
                colores.append(obtener_color("Verde"))
                lista_palabra_a_adivinar[pos] = pal_adiv[pos]

            elif ((pos == pos_2 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_1 and pos_2 == pal_adiv.index(intento[pos_2]))):
                colores.append(obtener_color("GrisOscuro"))

            elif (pos == pos_1 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                colores.append(obtener_color("Amarillo"))

            elif (pos == pos_2 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] not in pal_adiv:
            colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            colores.append(obtener_color("Amarillo"))

        elif intento[pos] == pal_adiv[pos]:
            colores.append(obtener_color("Verde"))
            lista_palabra_a_adivinar[pos] = pal_adiv[pos]

    return colores

def desarrollo_intentos(pal_adiv, intento, turnos, adivinar, palabras):
    '''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
        todos_turnos: para ir alternando los usuarios
    Salidas:
        Devuelve una lista con las palabras ingresadas.
    '''
    palabras_ingresadas=[]
    while len(palabras_ingresadas)<5 and pal_adiv not in palabras_ingresadas:
        orden_ingreso=len(palabras_ingresadas)
        #print(lista, palabras_ingresadas, orden_ingreso)
        colores = procesar_intento(pal_adiv, intento, adivinar)
        acumular_intentos(intento, orden_ingreso, colores, palabras, palabras_ingresadas)

        print("\nPalabra a adivinar: ", end = "")
        mostrar_palabra(adivinar)
        for intento in palabras:
            mostrar_palabra(intento)
            
        if pal_adiv not in palabras_ingresadas and len(palabras_ingresadas)<5:
            print("Es el turno de:", turnos[len(palabras_ingresadas)].upper())
            arriesgo=input("Arriesgo:")
            intento=validacion_intento_ingresado(arriesgo, palabras_ingresadas)
   
    return palabras_ingresadas

def acumular_intentos(palabra_ingresada, contador_intentos, colores, intentos_ingresados_list, intentos_ingresados_str):
    '''
    Función: acumular_intentos
    Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.
    Parámetros:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        intentos_ingresados: lista vacia.
    Salidas:
        Devuelve la lista cargada con las palabras ingresadas.

    '''
    intentos_ingresados_str.append(palabra_ingresada)
    for i in range(len(palabra_ingresada)):
        intentos_ingresados_list[contador_intentos][i] = colores[i] + palabra_ingresada[i]

def volver_a_jugar():
    '''
    Devuelve la respuesta de seguir jugando, de ser afirmativa devuelve el nuevo orden de los turnos.
    '''
    desea_jugar = input("\n¿Desea volver a jugar?(S/N):")
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input("¿Desea volver a jugar?(S/N):")
    
    return  desea_jugar

def nueva_partida(orden_jugador):
    ''' 
    Función que va alternando los turnos partida a partida
    '''
    orden_jugador.append(orden_jugador[1])
    del(orden_jugador[0])
    
    return orden_jugador

def determinar_ganador(usuarios):
    '''
    
    '''
    orden =sorted(usuarios.items(), key=lambda x:x[1], reverse=True)
    if orden[1][1] == orden[0][1]:
        print(f'\nLos jugadores empataron con un total de {orden[1][1]} puntos')
    else:    
        print(f'\nEl ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')
