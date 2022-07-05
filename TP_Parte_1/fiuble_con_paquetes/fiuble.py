from interfaz_usuario import *
from jugabilidad import *
from tiempo import *
from turnos_y_puntajes import *
from utiles import *
from validacion import *
from funcion_interfaz_grafica import*
from configuracion import *
from leer_archivos import *
import random
import time


#PRINCIPAL
def fiuble():
    CANTIDAD_INTENTOS = 5
    jugar = ''
    jugadores_y_puntos = interfaz_ingresar()  # acá deberiamos llamar a la interfaz grafica
    LONGITUD_PALABRAS,MAX_PARTIDAS,REINICIAR_PARTIDAS_CSV= leer_configuracion()
    turnos = orden_turnos(jugadores_y_puntos, CANTIDAD_INTENTOS)
    partida = 0
    archivo0 = open("Cuentos.txt")
    archivo1 = open("La araña negra - tomo 1.txt")
    archivo2 = open("Las 1000 Noches y 1 Noche.txt")
    diccionario_palabras_validas = {}
    palabras_validas(archivo0, archivo1, archivo2, diccionario_palabras_validas, LONGITUD_PALABRAS)

    while jugar in ('s','S', '') and partida < MAX_PARTIDAS:
        partida += 1
        lista_de_intentos_ingresados = []
        palabra_a_adivinar = generar_palabra_a_adivinar(diccionario_palabras_validas)
        lista_letras_palabra_adivinar = crear_lista_interrogantes(LONGITUD_PALABRAS)
        lista_letras_de_cada_intento = crear_lista_intentos(CANTIDAD_INTENTOS, lista_letras_palabra_adivinar) #Lista de listas, contiene los intentos ingresados,cada letra es un elemento.
        print('\nPalabra a adivinar: ', end = '')
        mostrar_palabra(lista_letras_palabra_adivinar)
        for intento in lista_letras_de_cada_intento:
            mostrar_palabra(intento)
        print('Es el turno de:',turnos[0].upper())
        inicio_cronometro = time.time()
        intento_sin_validar = input('Arriesgo:')
        intento = validacion_intento_ingresado(intento_sin_validar, lista_de_intentos_ingresados, diccionario_palabras_validas, LONGITUD_PALABRAS)
        lista_de_intentos_ingresados = desarrollo_intentos(palabra_a_adivinar, intento, turnos, lista_letras_palabra_adivinar, lista_letras_de_cada_intento, diccionario_palabras_validas, LONGITUD_PALABRAS) #Esta lista, es la lista de str de palabras ingresadas#
        fin_cronometro = time.time()
        tiempo = cronometro(inicio_cronometro, fin_cronometro)
        if palabra_a_adivinar in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            print(f'Palabra a adivinar: {palabra_a_adivinar[0]} {palabra_a_adivinar[1]} {palabra_a_adivinar[2]} {palabra_a_adivinar[3]} {palabra_a_adivinar[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos_ingresados,palabra_a_adivinar,jugadores_y_puntos,turnos)
        fecha,hora_finalizacion=fecha_y_hora() #Fecha y Hora
        jugar = volver_a_jugar()
        if jugar in ('s','S') and partida<= MAX_PARTIDAS:
            print(partida)
            turnos = cambio_turnos(turnos)
    determinar_ganador(jugadores_y_puntos)
fiuble()

