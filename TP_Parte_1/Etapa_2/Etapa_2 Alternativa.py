from utiles import *
'''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar, cadena de caracteres.
        intento: palabra ingresada por el usuario, cadena de caracteres.
    Salidas:
        Devuelve una lista con los colores correspondientes a las letras de la palabra ingresada.
    Precondiciones:
        Se asume que las palabras ingresadas existen, tienen 5 letras, no poseen números ni caracteres especiales.
'''
def desarrollo_intentos(pal_adiv, intento):
    colores = []
    for pos in range(len(pal_adiv)):
        if (pal_adiv.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == pal_adiv.index(intento[pos_2]))):
                colores.append(obtener_color("Verde"))

            elif ((pos == pos_2 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_1 and pos_2 == pal_adiv.index(intento[pos_2]))):
                colores.append(obtener_color("GrisOscuro"))

            elif (pos == pos_1 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                colores.append(obtener_color("Amarillo"))

            elif (pos == pos_2 and pos_1 != pal_adiv.index(intento[pos_1]) and pos_2 != pal_adiv.index(intento[pos_1])):
                colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] not in pal_adiv:
            colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            colores.append(obtener_color("Amarillo"))

        elif intento[pos] == pal_adiv[pos]:
            colores.append(obtener_color("Verde"))
    return colores
#ETAPA 2
'''
    Función: validacion
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra en mayúscula.
'''
def validacion(palabra_ingresada):
    palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    while not palabra_ingresada.isalpha() or palabra_ingresada.lower() not in obtener_palabras_validas():
        if not palabra_ingresada.isalpha() and len(palabra_ingresada) != 5:
            print("Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.")
        elif len(palabra_ingresada) != 5:
            print("Palabra inválida, tiene que ser de 5 letras.")
        elif palabra_ingresada not in obtener_palabras_validas() and palabra_ingresada.isalpha():
            print("Palabra inválida.")
        else:#if not palabra_ingresada.isalpha():
            print("Palabra inválida, no puede contener números ni caracteres especiales.")
        palabra_ingresada = input("Ingrese una palabra valida de 5 letras: ")
        palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    return palabra_ingresada.upper()

#ETAPA 2
'''
    Función: cambiar_tilde
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin caracteres con acentos.
'''
def cambiar_tilde(palabra_ingresada):
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = palabra_ingresada.maketrans(a, b)
    arriesgo = palabra_ingresada.translate(palabra_sin_acento)
    return arriesgo
    
#FUNCION PRINCIPAL
def fiuble():
    pal_adiv = "MARES"
    print("Palabra a adivinar: ? ? ? ? ?")
    intento = input("Arriesgo:")
    intento = validacion(intento)
    colores = desarrollo_intentos(pal_adiv, intento)

    print(f"\nPalabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]}")
    print("Arriesgo:", colores[0] + intento[0], colores[1] + intento[1], colores[2] + intento[2],
          colores[3] + intento[3], colores[4] + intento[4], obtener_color("Defecto"))

    if pal_adiv == intento:
        print('Ganaste!')
    else:
        print('Perdiste!')
fiuble()