from utiles import *


def mostrar_palabra(palabra_ingresada):
    """
    Recibe la palabra y la muestra en el formato deseado.
    """
    for letra in palabra_ingresada:
        print(letra + " " + obtener_color("Defecto"), end = "")
    print()


def ingreso_usuarios():
    """
    Nos retorna un diccionario creado con los nombres como claves y de valor sus puntajes
    """
    usuarios = {}
    usuario_1 = input("Ingreso usuario:")
    usuario_2 = input("Ingreso usuario:")
    usuarios[usuario_1] = 0
    usuarios[usuario_2] = 0

    return usuarios
