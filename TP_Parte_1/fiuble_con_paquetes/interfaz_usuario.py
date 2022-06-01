from utiles import *


def mostrar_palabra(palabra_ingresada):
    '''
    Función: mostrar_palabra
    Parametro:
        palabra_ingresada: Palabra que segun el momento de su ejecución varía.    
    Descripción: 
        Recibe una palabra y la muestra en el formato deseado.
    Salidas:
    '''
    for letra in palabra_ingresada:
        print(letra + ' ' + obtener_color('Defecto'), end = '')
    print()


def ingreso_jugadores():
    '''
    Función: ingreso_jugadores
    Parametro:
    Descripción: 
        Crea un diccionario con los nombres como claves y de valor sus puntajes.  
    Salidas:
        Nos retorna el diccionario.
    '''
    jugadores_y_puntos = {}
    jugadores_1 = input('Ingreso usuario:')
    jugadores_2 = input('Ingreso usuario:')
    jugadores_y_puntos[jugadores_1] = 0
    jugadores_y_puntos[jugadores_2] = 0

    return jugadores_y_puntos
