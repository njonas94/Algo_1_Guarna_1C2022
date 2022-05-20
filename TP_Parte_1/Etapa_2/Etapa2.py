def cambiar_tilde(palabra_ingresada):
    palabra_mayus = palabra_ingresada.upper()
    a = 'ÁÉÍÓÚÝÄËÏÖÜŸ'
    b = 'AEIOUYAEIOUY'
    palabra_sin_acento = palabra_mayus.maketrans(a, b)
    arriesgo = palabra_mayus.translate(palabra_sin_acento)
    return arriesgo


def validacion(palabra_ingresada):
    verificacion = False
    while not verificacion:
        if not palabra_ingresada.isalpha():
            print("La palabra no tiene que contener numero ni caracteres especiales")
        if len(palabra_ingresada) != 5:
            print("La palabra tiene que ser de 5 letras")
        palabra_ingresada = input("Ingrese una palabra valida de 5 letras: ")
        if palabra_ingresada.isalpha() and len(palabra_ingresada) == 5:
            verificacion = True
    return cambiar_tilde(palabra_ingresada)


def etepa_2():
    palabra_ingresada = input("Ingrese una palabra de 5 letras: ")
    print(validacion(palabra_ingresada))


etepa_2()
