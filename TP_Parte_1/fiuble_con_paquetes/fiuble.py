from interfaz_usuario import *
from jugabilidad import *
from utiles import *
from turnos_y_puntajes import *
from validacion import *
from interfaz_grafica import*
from configuracion import *
from procesar_archivos import *
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
    usuarios_datos = crear_diccionario_usuarios_datos(turnos)
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
        lista_de_intentos_ingresados = desarrollo_intentos(palabra_a_adivinar, intento, turnos, lista_letras_palabra_adivinar, lista_letras_de_cada_intento, diccionario_palabras_validas, LONGITUD_PALABRAS, CANTIDAD_INTENTOS) #Esta lista, es la lista de str de palabras ingresadas#
        fin_cronometro = time.time()
        tiempo = cronometro(inicio_cronometro, fin_cronometro)
        if palabra_a_adivinar in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            mostrar_palabra_adivinar(palabra_a_adivinar)
        puntaje(lista_de_intentos_ingresados,palabra_a_adivinar,jugadores_y_puntos,turnos)
        fecha,hora_finalizacion=fecha_y_hora() #Fecha y Hora
        cargar_hora(turnos,fecha,hora_finalizacion,usuarios_datos)
        lista_para_alda = cargar_aciertos_e_intentos(lista_de_intentos_ingresados, palabra_a_adivinar, usuarios_datos, turnos)
        jugar = volver_a_jugar()
        if jugar in ('s','S') and partida<= MAX_PARTIDAS:
            turnos = cambio_turnos(turnos)
    limpiar_archivo(REINICIAR_PARTIDAS_CSV)
    determinar_ganador(jugadores_y_puntos)
fiuble()

