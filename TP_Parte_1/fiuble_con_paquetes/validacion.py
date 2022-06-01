from utiles import *

def cambiar_tilde(palabra_ingresada):
    '''
    Función: cambiar_tilde
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin acentos.
    '''
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = palabra_ingresada.maketrans(a, b)
    arriesgo = palabra_ingresada.translate(palabra_sin_acento)

    return arriesgo

def no_es_alfabetico (palabra_ingresada):
    return not palabra_ingresada.isalpha()

def longitud_palabra (palabra_ingresada):
    return len(palabra_ingresada)!= 5

def validar_palabra (palabra_ingresada):
    return not no_es_alfabetico (palabra_ingresada) and palabra_ingresada not in obtener_palabras_validas()

def validar_ingreso (palabra_ingresada, intentos_ingresados_str):
    return palabra_ingresada.upper() in intentos_ingresados_str

def longitud_y_alfabetica(palabra_ingresada):
    return not palabra_ingresada.isalpha() and len(palabra_ingresada) != 5
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
