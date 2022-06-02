from utiles import *

def cambiar_tilde(intento_sin_validar):
    '''
    Función: cambiar_tilde
    Parámetro:
        intento_sin_validar: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin acentos.
    '''
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = intento_sin_validar.maketrans(a, b)
    intento_sin_validar_sin_tilde = intento_sin_validar.translate(palabra_sin_acento)

    return intento_sin_validar_sin_tilde

def no_es_alfabetico (intento_sin_validar):
    return not intento_sin_validar.isalpha()

def longitud_palabra (intento_sin_validar):
    return len(intento_sin_validar)!= 5

def validar_palabra (intento_sin_validar):
    return not no_es_alfabetico (intento_sin_validar) and intento_sin_validar not in obtener_palabras_validas()

def validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):
    return intento_sin_validar.upper() in lista_de_intentos_ingresados

def longitud_y_alfabetica(intento_sin_validar):
    return not intento_sin_validar.isalpha() and len(intento_sin_validar) != 5

def validacion_intento_ingresado(intento_sin_validar, lista_de_intentos_ingresados):
    '''
    Función: validacion_intento_ingresado
    Parámetro:
        intento_sin_validar: cadena de caracteres ingresado por el usuario.
        lista_de_intentos_ingresados: lista de cadenas de caracteres.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    intento_sin_validar = cambiar_tilde(intento_sin_validar.lower())
    while no_es_alfabetico (intento_sin_validar) or validar_palabra (intento_sin_validar) or validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):

        if longitud_y_alfabetica(intento_sin_validar):
            print("Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.")

        elif no_es_alfabetico (intento_sin_validar):
            print("La palabra no tiene que contener numero ni caracteres especiales.")

        elif longitud_palabra (intento_sin_validar): 
            print("La palabra tiene que ser de 5 letras.")

        elif validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):
            print("La palabra ya habia sido ingresada.")

        elif validar_palabra (intento_sin_validar):
            print("La palabra no se encuentra en la lista de palabras válidas.")

        intento_sin_validar = input("Ingrese una palabra valida de 5 letras: ")
        intento_sin_validar = cambiar_tilde(intento_sin_validar.lower())

    return intento_sin_validar.upper()
