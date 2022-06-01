from utiles import *

def validacion_intento_ingresado(palabra_ingresada, lista_palabras_ingresadas):
    '''
    Función: validar_intento_ingresado
    Descripción:   

    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        lista_palabras_ingresadas: lista de cadenas de caracteres.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    while not palabra_ingresada.isalpha() or palabra_ingresada.lower() not in obtener_palabras_validas() or (palabra_ingresada.upper() in lista_palabras_ingresadas):
        if not palabra_ingresada.isalpha() and len(palabra_ingresada) != 5:
            print('Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.')
        elif len(palabra_ingresada) != 5:
            print('Palabra inválida, tiene que ser de 5 letras.')
        elif palabra_ingresada not in obtener_palabras_validas() and palabra_ingresada.isalpha():
            print('Palabra inválida.')
        elif palabra_ingresada.upper() in lista_palabras_ingresadas:
            print('La palabra ya habia sido ingresada.')
        else:#if not palabra_ingresada.isalpha():
            print('Palabra inválida, no puede contener números ni caracteres especiales.')
        palabra_ingresada = input('Ingrese una palabra valida de 5 letras: ')
        palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    
    return palabra_ingresada.upper()

def cambiar_tilde(palabra_ingresada):
    '''
    Función: cambiar_tilde
    Descripción: 

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
