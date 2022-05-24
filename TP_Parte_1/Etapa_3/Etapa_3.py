import random
from utiles import *


def generar_palabra_a_adivinar():
    """
    Nos retorna la palabra a adivinar
    """
    palabras_validas = obtener_palabras_validas()

    return random.choice(palabras_validas)


def acumular_intentos(palabra_ingresada, contador_intentos, colores, intentos_ingresados_list, intentos_ingresados_str):
    intentos_ingresados_str.append(palabra_ingresada)
    for i in range(len(palabra_ingresada)):
        intentos_ingresados_list[contador_intentos][i] = colores[i] + palabra_ingresada[i]

    return


def mostrar_palabra(lista_palabra_ingresada):
    """
    Nos muestra la palabra una al lado de la otra
    """
    for letra in lista_palabra_ingresada:
        print(letra + " " + obtener_color("Defecto"), end = "")
    print()

    return


def dar_formato_al_intento(palabra_ingresada):
    """
    Recibimos la palabra ingresada y la retornamos sin tildes
    """
    palabra_mayus = palabra_ingresada.upper()
    a = 'ÁÉÍÓÚÝÄËÏÖÜŸ'
    b = 'AEIOUYAEIOUY'
    palabra_sin_acento = palabra_mayus.maketrans(a, b)
    arriesgo = palabra_mayus.translate(palabra_sin_acento)

    return arriesgo


def validacion(palabra_ingresada, intentos_ingresados_str):
    """
    Recibimos la palabra ingresada y verificamos que cumpla con las condiciones
    """
    verificacion = False
    if not palabra_ingresada.isalpha():
        print("La palabra no tiene que contener numero ni caracteres especiales.")
    if len(palabra_ingresada) != 5:
        print("La palabra tiene que ser de 5 letras.")
    if dar_formato_al_intento(palabra_ingresada).lower() not in obtener_palabras_validas():
        print("La palabra no se encuentra en la lista de palabras válidas.")
    if palabra_ingresada.upper() in intentos_ingresados_str:
        print("La palabra ya habia sido ingresada.")
    #Consultar al profe sobre como tratar el if que quedo excesivamente largo    
    if palabra_ingresada.isalpha() and len(palabra_ingresada) == 5 and dar_formato_al_intento(palabra_ingresada).lower() in obtener_palabras_validas() and palabra_ingresada.upper() not in intentos_ingresados_str:
        verificacion = True

    return verificacion


def procesar_intento(pal_adiv, intento, lista_palabra_a_adivinar):
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
                lista_palabra_a_adivinar[pos] = pal_adiv[pos]

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
            lista_palabra_a_adivinar[pos] = pal_adiv[pos]

        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            color_2 = obtener_color("Amarillo")
            colores.append(color_2)

        elif intento[pos] not in pal_adiv:
            color_3 = obtener_color("GrisOscuro")
            colores.append(color_3)

    return colores


def juego_terminado(intentos_ingresados_list, palabra_a_adivinar):
    print("Palabra a adivinar: ", end = "")
    mostrar_palabra(palabra_a_adivinar)
    for intento in intentos_ingresados_list:
        mostrar_palabra(intento)

    return

def main():
    palabra_a_adivinar = generar_palabra_a_adivinar().upper()
    intentos_ingresados_str = []
    intentos_ingresados_list = [["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"],
                           ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"]]
    lista_palabra_a_adivinar = ["?", "?", "?", "?", "?"]
    contador_intentos = 0
    victoria = False
    while contador_intentos < 5 and victoria == False:
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(lista_palabra_a_adivinar)
        for intento in intentos_ingresados_list:
            mostrar_palabra(intento)
        arriesgo = input("Arriesgo: ")
        if validacion(arriesgo, intentos_ingresados_str):
            arriesgo = dar_formato_al_intento(arriesgo)
            colores = procesar_intento(palabra_a_adivinar, arriesgo, lista_palabra_a_adivinar)
            acumular_intentos(arriesgo, contador_intentos, colores, intentos_ingresados_list, intentos_ingresados_str)
            contador_intentos += 1
            if palabra_a_adivinar == arriesgo:
                juego_terminado(intentos_ingresados_list, palabra_a_adivinar)
                print("Ganaste!")
                victoria = True
            elif contador_intentos == 5:
                juego_terminado(intentos_ingresados_list, palabra_a_adivinar)
                print("Perdiste!")
        print()

    return


main()

