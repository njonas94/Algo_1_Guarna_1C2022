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

    
def nombres_repetidos(CASO, jugador_1, jugador_2): #única función llamada por la función no modularizada dentro de ingreso_jugadores()
    '''
    Responsable: CASTRO, CARLA
    Función: nombres_repetidos
    Parámetros:
        CASO: variable constante, número.
        jugador_1: cadena de caracteres.
        jugador_2: cadena de caracteres.
    Salida:
        Devuelve el nuevo nombre que tendrá el jugador con nombre inválido o repetido.
    '''
    while jugador_1 == jugador_2:
        if CASO == 0:
            print(f'Nombre " {jugador_1} " no disponible. Ingrese un nombre distinto.')
            jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
            jugador = jugador_2
            
        elif CASO == 1:
            print(f'Nombre " {jugador_2} " no disponible. Ingrese un nombre distinto.')
            jugador_1 = input('\nIngrese el nombre del 1er usuario:').upper()
            jugador = jugador_1
                        
    return jugador       


def nombrar_primer_jugador(jugador_2):
    '''
    Responsable: CASTRO, CARLA
    Función: nombrar_primer_jugador
    Parámetros:
        jugador_2: cadena de caracteres.
    Salida:
        Devuelve el nombre del jugador_1.
    '''
    jugador_1 = input('\nIngrese el nombre del 1er usuario:').upper()
    if jugador_1 == jugador_2:
        CASO = 1
        jugador_1 = nombres_repetidos(CASO, jugador_1, jugador_2)
    
    return jugador_1


def nombrar_segundo_jugador(jugador_1):
    '''
    Responsable: CASTRO, CARLA
    Función: nombrar_segundo_jugador
    Parámetros:
        jugador_1: cadena de caracteres.
    Salida:
        Devuelve el nombre del jugador_2.
    '''
    jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
    if jugador_2 == jugador_1:
        CASO = 0
        jugador_2 = nombres_repetidos(CASO, jugador_1, jugador_2)
        
    return jugador_2

    
def validar_nombres_ingresados(jugador_1, jugador_2, jugadores_y_puntos):
    '''
    Responsable: CASTRO, CARLA
    Función: validar_nombres_ingresados
    Parámetros:
        jugador_1: cadena de caracteres.
        jugador_2: cadena de caracteres.
        jugadores_y_puntos: diccionario vacio.
    Salida:
        Devuelve el diccionario cargado.
    '''
    while not jugador_1.isalpha() or not jugador_2.isalpha() or jugador_2 == jugador_1:
        
        if not jugador_1.isalpha() and not jugador_2.isalpha(): #Usuarios inválidos
            print('Nombres inválidos, intente nuevamente. No usar números ni caracteres especiales.')
            jugador_1 = input('\nIngrese el nombre del 1er usuario:').upper()
            jugador_2 = input('Ingrese el nombre del 2do usuario:').upper()
            if jugador_2 == jugador_1 and jugador_1.isalpha():
                CASO = 0
                jugador_2 = nombres_repetidos(CASO, jugador_1, jugador_2)
                    
        elif not jugador_1.isalpha() and jugador_2.isalpha():
            print(f'Nombre "{jugador_1}" inválido, no usar números ni caracteres especiales. Nombre "{jugador_2}" no disponible.')
            jugador_1 = nombrar_primer_jugador(jugador_2)
            
        elif not jugador_2.isalpha() and jugador_1.isalpha():
            print(f'Nombre "{jugador_2}" inválido, no usar números ni caracteres especiales. Nombre "{jugador_1}" no disponible.')
            jugador_2 = nombrar_segundo_jugador(jugador_1)
                
        elif jugador_2 == jugador_1:
            print(f'Nombre "{jugador_1}" no disponible. Ingrese un nombre distinto.')
            jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
    
    jugadores_y_puntos[jugador_1] = 0
    jugadores_y_puntos[jugador_2] = 0
    
    return jugadores_y_puntos    
    
       
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
    validar_nombres_ingresados(jugador_1, jugador_2, jugadores_y_puntos)
    
        #VERIFICACION AL NOMBRAR USUARIOS, NO MODULARIZADO
#     while not jugador_1.isalpha() or not jugador_2.isalpha() or jugador_2 == jugador_1:
#         if not jugador_1.isalpha() and not jugador_2.isalpha(): #Usuarios inválidos
#             print('Nombres inválidos, intente nuevamente. No usar números ni caracteres especiales.')
#             jugador_1 = input('\nIngrese el nombre del 1er usuario:').upper()
#             jugador_2 = input('Ingrese el nombre del 2do usuario:').upper()
#             if jugador_2 == jugador_1 and jugador_1.isalpha():
#                 CASO = 0
#                 jugador_2 = nombres_repetidos(CASO, jugador_1, jugador_2)
#                     
#         elif not jugador_1.isalpha() and jugador_2.isalpha():
#             print(f'Nombre "{jugador_1}" inválido, no usar números ni caracteres especiales. Nombre "{jugador_2}" no disponible.')
#             jugador_1 = input('\nIngrese el nombre del 1er usuario:').upper()
#             if jugador_1 == jugador_2:
#                 CASO = 1
#                 jugador_1 = nombres_repetidos(CASO, jugador_1, jugador_2)
#             
#         elif not jugador_2.isalpha() and jugador_1.isalpha():
#             print(f'Nombre "{jugador_2}" inválido, no usar números ni caracteres especiales. Nombre "{jugador_1}" no disponible.')
#             jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
#             if jugador_2 == jugador_1:
#                 CASO = 0
#                 jugador_2 = nombres_repetidos(CASO, jugador_1, jugador_2)
#                 
#         elif jugador_2 == jugador_1:
#             print(f'Nombre "{jugador_1}" no disponible. Ingrese un nombre distinto.')
#             jugador_2 = input('\nIngrese el nombre del 2er usuario:').upper()
#         
#     jugadores_y_puntos[jugador_1] = 0
#     jugadores_y_puntos[jugador_2] = 0

    return jugadores_y_puntos
