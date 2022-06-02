from utiles import *


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

    
def validar_nombres_ingresados(jugador_1, jugador_2):
    '''
    Responsable: CASTRO, CARLA
    Función: validar_nombres_ingresados
    Parámetros:
        jugador_1: cadena de caracteres.
        jugador_2: cadena de caracteres.
    Salida:
        Devuelve el nombre del jugador_2.
    '''
    while jugador_2 == jugador_1:
        print(f'Nombre "{jugador_1}" no disponible. Ingrese un nombre distinto.')
        jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
       
    return jugador_2    
    
       
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
    jugador_2 = validar_nombres_ingresados(jugador_1, jugador_2)    
    
    jugadores_y_puntos[jugador_1] = 0
    jugadores_y_puntos[jugador_2] = 0

    return jugadores_y_puntos
