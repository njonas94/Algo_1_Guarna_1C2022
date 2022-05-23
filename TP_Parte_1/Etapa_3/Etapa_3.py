import random
from utiles import *


def generar_palabra_a_adivinar():
    """
    Nos retorna la palabra a adivinar
    """
    palabras_validas = obtener_palabras_validas()

    return random.choice(palabras_validas)


def acumular_intentos(palabra_ingresada, contador_intentos, intentos_ingresados):
    for i in range(len(palabra_ingresada)):
        intentos_ingresados[contador_intentos][i] = palabra_ingresada[i]

    return


def mostrar_palabra(lista_palabra_ingresada):
    """
    Nos muestra la palabra una al lado de la otra
    """
    for letra in lista_palabra_ingresada:
        print(letra + " ", end = "")
    print()

    return


def cambiar_tilde(palabra_ingresada):
    """
    Recibimos la palabra ingresada y la retornamos sin tildes
    """
    palabra_mayus = palabra_ingresada.upper()
    a = 'ÁÉÍÓÚÝÄËÏÖÜŸ'
    b = 'AEIOUYAEIOUY'
    palabra_sin_acento = palabra_mayus.maketrans(a, b)
    arriesgo = palabra_mayus.translate(palabra_sin_acento)

    return arriesgo


def validacion(palabra_ingresada, intentos_ingresados):
    """
    Recibimos la palabra ingresada y verificamos que cumpla con las condiciones
    """
    verificacion = False
    if not palabra_ingresada.isalpha():
        print("La palabra no tiene que contener numero ni caracteres especiales.")
    if len(palabra_ingresada) != 5:
        print("La palabra tiene que ser de 5 letras.")
    if palabra_ingresada not in obtener_palabras_validas():
        print("La palabra no se encuentra en la lista de palabras válidas.")
    if palabra_ingresada in intentos_ingresados:
        print("La palabra ya habia sido ingresada.")
    if palabra_ingresada.isalpha() and len(
            palabra_ingresada) == 5 and palabra_ingresada in obtener_palabras_validas() and palabra_ingresada not in intentos_ingresados:
        verificacion = True

    return verificacion


def procesar_intento(pal_adiv, intento):
    """
    Este es el proceso para ver si las letras estan, se repiten o no estan en la palabra a adivinar
    """
    colores = []
    for pos in range(len(pal_adiv)):
        if (pal_adiv.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == pal_adiv.index(intento[pos_2]))):
                color_1 = obtener_color("Verde")
                colores.append(color_1)

            elif ((pos == pos_2 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_1 and pos_2 == pal_adiv.index(intento[pos_2]))):
                color_3 = obtener_color("GrisOscuro")
                colores.append(color_3)

            elif (pos == pos_1 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                color_2 = obtener_color("Amarillo")
                colores.append(color_2)

            elif (pos == pos_2 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                color_3 = obtener_color("GrisOscuro")
                colores.append(color_3)

        elif intento[pos] == pal_adiv[pos]:
            color_1 = obtener_color("Verde")
            colores.append(color_1)

        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            color_2 = obtener_color("Amarillo")
            colores.append(color_2)

        elif intento[pos] not in pal_adiv:
            color_3 = obtener_color("GrisOscuro")
            colores.append(color_3)

    return colores


def main():
    palabra_a_adivinar = generar_palabra_a_adivinar()
    intentos_ingresados = [["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"],
                           ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"]]
    lista_palabra_a_adivinar = ["?", "?", "?", "?", "?"]
    contador_intentos = 0
    while contador_intentos < 5:
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(lista_palabra_a_adivinar)
        for intento in intentos_ingresados:
            mostrar_palabra(intento)
        arriesgo = input("Arriesgo: ")
        if validacion(arriesgo, intentos_ingresados):
            arriesgo = cambiar_tilde(arriesgo)
            acumular_intentos(arriesgo, contador_intentos, intentos_ingresados)
            contador_intentos += 1
            if palabra_a_adivinar == arriesgo:
                print('Ganaste!')
            elif contador_intentos == 5:
                print('Perdiste!')

    return


main()

"""
Pruebas

print(intentos_ingresados)
print(intentos_ingresados[0])
print(intentos_ingresados[1])

print("Arriesgo:",colores[0] + intento[0].upper(),colores[1] + intento[1].upper(), colores[2] + intento[2].upper(), colores[3] + intento[3].upper(), colores[4] + intento[4].upper(), obtener_color ("Defecto"))


"""
