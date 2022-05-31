from interfaz_usuario import *
from jugabilidad import *
from tiempo import *
from turnos_y_puntajes import *
from utiles import *
from validacion import *

import random
import time

#PRINCIPAL
def fiuble():
    LONGITUD_PALABRAS = 5
    CANTIDAD_INTENTOS = 5
    jugar = ''
    usuarios_y_puntaje = ingreso_usuarios()#Diccionario: claves: nombres de usuario y valor: puntos acumulados
    turnos = orden_turnos(usuarios_y_puntaje)
    while jugar in ('s','S', ''):
        lista_de_intentos_ingresados = []
        pal_adiv = generar_palabra_a_adivinar()
        adivinar = crear_lista_interrogantes(LONGITUD_PALABRAS)
        palabras = crear_lista_intentos(CANTIDAD_INTENTOS, adivinar)
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(adivinar)
        for intento in palabras:
            mostrar_palabra(intento)
        print("Es el turno de:",turnos[0].upper())
        inicio = time.time()
        intento = input("Arriesgo:")
        intento = validacion_intento_ingresado(intento, lista_de_intentos_ingresados)
        lista_de_intentos_ingresados = desarrollo_intentos(pal_adiv, intento, turnos, adivinar, palabras) #Esta lista, es la lista de str de palabras ingresadas#
        fin = time.time()
        tiempo = cronometro(inicio, fin)
        if pal_adiv in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            print(f'Palabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos_ingresados,pal_adiv,usuarios_y_puntaje,turnos)
        jugar, turnos = volver_a_jugar(turnos)
    determinar_ganador(usuarios_y_puntaje)
fiuble()

