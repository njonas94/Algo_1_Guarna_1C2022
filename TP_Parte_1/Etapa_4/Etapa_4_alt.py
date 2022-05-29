from functools import partialmethod
from utiles import *
import random
import time


def generar_palabra_a_adivinar():
    """
    Devuelve la palabra a adivinar en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.

    """
    palabras_validas = obtener_palabras_validas()

    return random.choice(palabras_validas)


def acumular_intentos(palabra_ingresada, contador_intentos, colores, intentos_ingresados_list, intentos_ingresados_str):
    """
    Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.

    """
    intentos_ingresados_str.append(palabra_ingresada)
    for i in range(len(palabra_ingresada)):
        intentos_ingresados_list[contador_intentos][i] = colores[i] + palabra_ingresada[i]


def mostrar_palabra(lista_palabra_ingresada):
    """
    Muestra por pantalla las palabras en el formato deseado.
    """
    for letra in lista_palabra_ingresada:
        print(letra + " " + obtener_color("Defecto"), end = "")
    print()



def dar_formato_al_intento(palabra_ingresada):
    """
    Recibe un string con tildes y devuelve sin tildes y en mayuscula.
    """
    palabra_mayus = palabra_ingresada.upper()
    a = 'ÁÉÍÓÚÝÄËÏÖÜŸ'
    b = 'AEIOUYAEIOUY'
    palabra_sin_acento = palabra_mayus.maketrans(a, b)
    arriesgo = palabra_mayus.translate(palabra_sin_acento)

    return arriesgo


def validacion(palabra_ingresada, intentos_ingresados_str):
    """
    Devuelve True o False si la palabra ingresada cumple con lo solicitado en las reglas del juego e informa por terminal en caso de errores.
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
    Procesa el intento ingresado, creando una lista con el correspondiente color asignado a cada letra en el mismo indice que el string ingresado.
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
    """
    Muestra en terminal la "Palabra a adivinar" y los intentos.
    """
    print("Palabra a adivinar: ", end = "")
    mostrar_palabra(palabra_a_adivinar)
    for intento in intentos_ingresados_list:
        mostrar_palabra(intento)


def cronometro(comienzo, final):
    """
    Se encarga de guardar el tiempo tardado en jugar.
    """
    tiempo_tardado = (final-comienzo)
    if tiempo_tardado >= 60:
        minutos = tiempo_tardado//60
        segundos = round(tiempo_tardado%60,0)
    else:
        minutos = 0
        segundos = round(tiempo_tardado,0)    

    return minutos, segundos

def puntaje(intentos_ingresados_str,palabra_a_adivinar,puntos_por_partida):
    """
    Asigna el puntaje correspondiente a la partida, y lo guarda en la lista de puntos por partida.
    """
    valores=[50,40,30,20,10,-100]
    if palabra_a_adivinar not in intentos_ingresados_str and len(intentos_ingresados_str)==5:
        puntos_obtenidos = -100
    elif palabra_a_adivinar in intentos_ingresados_str:
        if len(intentos_ingresados_str)==1:
            puntos_obtenidos = valores[0]
        elif len(intentos_ingresados_str)==2:
            puntos_obtenidos = valores[1]
        elif len(intentos_ingresados_str)==3:
            puntos_obtenidos = valores[2]
        elif len(intentos_ingresados_str)==4:
            puntos_obtenidos = valores[3]
        elif len(intentos_ingresados_str)==5:
            puntos_obtenidos = valores[4]

    puntos_por_partida.append(puntos_obtenidos)

def mostrar_puntaje(puntos_por_partida):
    """
    Muestra por pantalla el puntaje obtenido/perdido, y en caso de que corresponda, el acumulado.
    """
    acumulados = 0
    puntaje_ultima_partida = puntos_por_partida[-1]
    if len(puntos_por_partida) > 1:
        acumulados = sum(puntos_por_partida)
        if puntaje_ultima_partida>0:
            print(f"Obtuviste un total de {puntaje_ultima_partida} puntos, tenes acumulados {acumulados} puntos")
        else:
            print(f"Perdiste un total de {-puntaje_ultima_partida} puntos, tenes acumulados {acumulados} puntos")
    else:
        if puntaje_ultima_partida>0:
            print(f"Obtuviste un total de {puntaje_ultima_partida} puntos.")
        else:
            print(f"Perdiste un total de {-puntaje_ultima_partida} puntos.")


def main():
    partida = 0
    desea_jugar = True
    partida_terminada = False
    puntos_por_partida = []

    while desea_jugar:

        if partida_terminada == True:
            volver_a_jugar = input("¿Desea volver a jugar?(S/N):")
            if volver_a_jugar in ["s", "S"]:
                partida_terminada = False
            elif volver_a_jugar in ["n", "N"]:
                desea_jugar = False
        else:    
            palabra_a_adivinar = generar_palabra_a_adivinar().upper()
            intentos_ingresados_str = []
            intentos_ingresados_list = [["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"],
                                ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"]]
            lista_palabra_a_adivinar = ["?", "?", "?", "?", "?"]
            contador_intentos = 0
            victoria = False
            inicio_tiempo = time.time()

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
                        victoria = True
                        final_tiempo = time.time()
                        minutos_tardados, segundos_tardados = cronometro(inicio_tiempo, final_tiempo)
                        print("Ganaste! Tardaste", minutos_tardados ,"minutos y", segundos_tardados ,"segundos")
                        puntaje(intentos_ingresados_str, palabra_a_adivinar, puntos_por_partida)
                        mostrar_puntaje(puntos_por_partida)
                        partida_terminada = True
                    elif contador_intentos == 5:
                        juego_terminado(intentos_ingresados_list, palabra_a_adivinar)
                        print("Perdiste!")
                        puntaje(intentos_ingresados_str, palabra_a_adivinar, puntos_por_partida)
                        mostrar_puntaje(puntos_por_partida)
                        partida_terminada = True

                print()

    return


main()

