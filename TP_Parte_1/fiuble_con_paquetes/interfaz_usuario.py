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
