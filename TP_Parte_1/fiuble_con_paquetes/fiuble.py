from interfaz_usuario import *
from jugabilidad import *
from tiempo import *
from turnos_y_puntajes import *
from utiles import *
from validacion import *

import random
import time
'''
cambiar:
- nueva partida en jugabilidad falta aclarar la salida
- contador puntajes en turnos y puntajes falta aclarar un parametro
'''
#PRINCIPAL
def fiuble():
    LONGITUD_PALABRAS = 5
    CANTIDAD_INTENTOS = 5
    jugar = ''
    usuarios_y_puntaje = ingreso_jugadores()
    turnos = orden_turnos(usuarios_y_puntaje, CANTIDAD_INTENTOS)
    while jugar in ('s','S', ''):
        lista_de_intentos_ingresados = []
        palabra_a_adivinar = generar_palabra_a_adivinar()
        lista_letras_palabra_adivinar = crear_lista_interrogantes(LONGITUD_PALABRAS)
        lista_letras_de_cada_intento = crear_lista_intentos(CANTIDAD_INTENTOS, lista_letras_palabra_adivinar) #Lista de listas, contiene los intentos ingresados,cada letra es un elemento.
        print('\nPalabra a adivinar: ', end = '')
        mostrar_palabra(lista_letras_palabra_adivinar)
        for intento in lista_letras_de_cada_intento:
            mostrar_palabra(intento)
        print('Es el turno de:',turnos[0].upper())
        inicio_cronometro = time.time()
        arriesgo = input('Arriesgo:')
        intento = validacion_intento_ingresado(arriesgo, lista_de_intentos_ingresados)
        lista_de_intentos_ingresados = desarrollo_intentos(palabra_a_adivinar, intento, turnos, lista_letras_palabra_adivinar, lista_letras_de_cada_intento) #Esta lista, es la lista de str de palabras ingresadas#
        fin_cronometro = time.time()
        tiempo = cronometro(inicio_cronometro, fin_cronometro)
        if palabra_a_adivinar in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            print(f'Palabra a adivinar: {palabra_a_adivinar[0]} {palabra_a_adivinar[1]} {palabra_a_adivinar[2]} {palabra_a_adivinar[3]} {palabra_a_adivinar[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos_ingresados,palabra_a_adivinar,usuarios_y_puntaje,turnos)
        jugar = volver_a_jugar()
        if jugar in ('s','S'):
            turnos = cambio_turnos(turnos)
    determinar_ganador(usuarios_y_puntaje)
fiuble()

