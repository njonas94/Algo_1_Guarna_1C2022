import random
from utiles import *

palabra_ingresada = ""
lista_palabra_a_adivinar = ["?", "?", "?", "?", "?"]
intentos_ingresados = [obtener_color("Verde") + "A",obtener_color ("Defecto")]


def generar_palabra_a_adivinar():
    palabras_validas = obtener_palabras_validas()
    
    return random.choice(palabras_validas)

palabra_a_adivinar = generar_palabra_a_adivinar()

def acumular_intentos(palabra_ingresada):
    if palabra_ingresada not in intentos_ingresados:
        intentos_ingresados.append(palabra_ingresada)
    return

def mostrar_juego(lista_palabra_ingresada):
    print("Palabra a adivinar: ", end="")
    for letra in lista_palabra_ingresada:
        print(letra + " ", end= "")

    
    
    return

def main():
    while True:
        mostrar_juego()
        break

    return

#mostrar_juego(lista_palabra_a_adivinar)
"""
Pruebas

print(intentos_ingresados)
print(intentos_ingresados[0])
print(intentos_ingresados[1])
print("prueba")

"""