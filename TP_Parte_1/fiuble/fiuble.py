from utiles import *
import random
import time

def generar_palabra_a_adivinar():
    '''
    Función: generar_palabra_a_adivinar
        Devuelve la palabra a adivinar en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.
    Salidas:
        Devuelve la palabra seleccionada aleatoriamente en mayúscula.
    '''
    palabras_validas = obtener_palabras_validas()
    palabra=random.choice(palabras_validas)

    return palabra.upper()

def validacion_intento_ingresado(palabra_ingresada, palabras_ingresadas):
    '''
    Función: validar_intento_ingresado
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    while not palabra_ingresada.isalpha() or palabra_ingresada.lower() not in obtener_palabras_validas() or (palabra_ingresada.upper() in palabras_ingresadas):
        if not palabra_ingresada.isalpha() and len(palabra_ingresada) != 5:
            print("Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.")
        elif len(palabra_ingresada) != 5:
            print("Palabra inválida, tiene que ser de 5 letras.")
        elif palabra_ingresada not in obtener_palabras_validas() and palabra_ingresada.isalpha():
            print("Palabra inválida.")
        elif palabra_ingresada.upper() in palabras_ingresadas:
            print("La palabra ya habia sido ingresada.")
        else:#if not palabra_ingresada.isalpha():
            print("Palabra inválida, no puede contener números ni caracteres especiales.")
        palabra_ingresada = input("Ingrese una palabra valida de 5 letras: ")
        palabra_ingresada = cambiar_tilde(palabra_ingresada.lower())
    
    return palabra_ingresada.upper()

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

def crear_lista_interrogantes(LONGITUD_PALABRAS):
    '''
    Autor : Aldair Torres
    Pre: recibe la palabra a adivinar para saber su longitud
    Post: Nos devuelve una lista conformada por signos de interrogacion
    '''
    lista_interrogantes = []
    for i in range(LONGITUD_PALABRAS):
        lista_interrogantes.append('?')
    
    return lista_interrogantes

def crear_lista_intentos(CANTIDAD_INTENTOS, lista_interrogantes):
    '''
    Autor: Aldair Torres
    Pre: recibe una cantidad de intentos y una lista con interrogantes
    Post: Nos devuelve una lista de listas en donde se almacenas los intentos
    '''
    lista_intentos = []
    for i in range(CANTIDAD_INTENTOS):
        lista_intentos.append(lista_interrogantes.copy())
    
    return lista_intentos

def procesar_intento(pal_adiv, intento, lista_palabra_a_adivinar):
    '''
    Procesa el intento ingresado, creando una lista con el correspondiente color asignado a cada letra en el mismo indice que el string ingresado.
    '''
    colores = []
    for pos in range(len(pal_adiv)):
        if (pal_adiv.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == pal_adiv.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == pal_adiv.index(intento[pos_2]))):
                colores.append(obtener_color("Verde"))
                lista_palabra_a_adivinar[pos] = pal_adiv[pos]

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
            lista_palabra_a_adivinar[pos] = pal_adiv[pos]

    return colores

def desarrollo_intentos(pal_adiv, intento, turnos, adivinar, palabras):
    '''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
        todos_turnos: para ir alternando los usuarios
    Salidas:
        Devuelve una lista con las palabras ingresadas.
    '''
    palabras_ingresadas=[]
    while len(palabras_ingresadas)<5:
        orden_ingreso=len(palabras_ingresadas)
        #print(lista, palabras_ingresadas, orden_ingreso)
        colores = procesar_intento(pal_adiv, intento, adivinar)
        acumular_intentos(intento, orden_ingreso, colores, palabras, palabras_ingresadas)

        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(adivinar)
        for intento in palabras:
            mostrar_palabra(intento)
            
        if pal_adiv not in palabras_ingresadas and len(palabras_ingresadas)<5:
            print("Es el turno de:", turnos[len(palabras_ingresadas)].upper())
            arriesgo=input("Arriesgo:")
            intento=validacion_intento_ingresado(arriesgo, palabras_ingresadas)
   
    return palabras_ingresadas

def acumular_intentos(palabra_ingresada, contador_intentos, colores, intentos_ingresados_list, intentos_ingresados_str):
    '''
    Función: acumular_intentos
    Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.
    Parámetros:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        intentos_ingresados: lista vacia.
    Salidas:
        Devuelve la lista cargada con las palabras ingresadas.

    '''
    intentos_ingresados_str.append(palabra_ingresada)
    for i in range(len(palabra_ingresada)):
        intentos_ingresados_list[contador_intentos][i] = colores[i] + palabra_ingresada[i]

def cronometro(comienzo, final):
    '''
    Función: cronometro
    Parámetros:
        comienzo: inicia contador.
        final: detiene contador.
    Salidas:
        Devuelve los minutos y segundos tardados en finalizar el juego.
    '''
    tiempo_tardado=(final-comienzo)
    if tiempo_tardado>=60:
        minutos=tiempo_tardado//60
        segundos=round(tiempo_tardado%60,0)
        tiempo=[minutos, segundos]
    else:
        minutos=0
        segundos=round(tiempo_tardado,0)
        tiempo=[minutos, segundos]
    
    return tiempo

def puntaje(lista,adivinar,usuarios,turnos):
    '''
    Función: puntaje
    Parámetros:
        lista: lista de cadenas de caracteres.
        adivinar: cadena de caracteres, palabra a adivinar.
        todos_turnos: lista vacia.
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
    '''
    valores=[50,40,30,20,10,-50,-100]
    if adivinar not in lista and len(lista)==5:
        usuarios[turnos[0]]+= valores[-1]
        usuarios[turnos[1]]+= valores[-2]
        print(f"{turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {usuarios[turnos[0]]} puntos.")
        print(f"{turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {usuarios[turnos[1]]} puntos.")
    elif adivinar in lista:
        if len(lista)==1:
            puntos_obtenidos=valores[0]
        elif len(lista)==2:
            puntos_obtenidos=valores[1]
        elif len(lista)==3:
            puntos_obtenidos=valores[2]
        elif len(lista)==4:
            puntos_obtenidos=valores[3]
        elif len(lista)==5:
            puntos_obtenidos=valores[4]
        indice = len(lista)-1
        usuarios = contador_puntajes (puntos_obtenidos,usuarios,turnos,indice)
    
    return usuarios

def contador_puntajes (puntos_obtenidos,usuarios,turnos,indice):
    ''' 
    Funcion que acumula el puntaje para cada jugador.
    '''
    jugador_acierto = turnos[indice]
    if indice ==0:
        jugador_fallo = turnos[indice-2]
    else:
        jugador_fallo = turnos[indice-1]
    usuarios[jugador_acierto] += puntos_obtenidos
    if puntos_obtenidos > 0:
        usuarios[jugador_fallo] += -puntos_obtenidos
        print(f"{jugador_acierto.upper()}, ha ganado: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_acierto]} puntos.")
        print(f"{jugador_fallo.upper()}, ha perdido: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_fallo]} puntos.")
    
    return usuarios
 
def volver_a_jugar(turnos):
    '''
    Devuelve la respuesta de seguir jugando, de ser afirmativa devuelve el nuevo orden de los turnos.
    '''
    desea_jugar = input("\n¿Desea volver a jugar?(S/N):")
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input("¿Desea volver a jugar?(S/N):")
    if desea_jugar in ('s','S'):
        turnos = nueva_partida(turnos)
    
    return  desea_jugar, turnos

def ingreso_usuarios():
    ''' 
    Carga un diccionario, las claves son los ususarios y el valor acumulara sus respectivos puntajes.
    '''
    usuarios = {}
    usuario_1 = input("Ingreso usuario:")
    usuario_2 = input("Ingreso usuario:")
    usuarios[usuario_1] = 0
    usuarios[usuario_2] = 0
    
    return usuarios

def orden_turnos (usuarios):
    ''' 
    Generador de turnos 
    '''
    turnos = []
    nombre = list(usuarios.keys())
    master=random.choice(nombre)
    indice = nombre.index(master)
    for i in range(5):
        if i in (0,2,4):
            turnos.append(master)              
        else:
            turnos.append(nombre[indice-1])
    
    return turnos

def nueva_partida(orden_jugador):
    ''' 
    Función que va alternando los turnos partida a partida
    '''
    orden_jugador.append(orden_jugador[1])
    del(orden_jugador[0])
    
    return orden_jugador

def determinar_ganador(usuarios):
    orden =sorted(usuarios.items(), key=lambda x:x[1], reverse=True)
    if orden[1][1] == orden[0][1]:
        print(f'\nLos jugadores empataron con un total de {orden[1][1]} puntos')
    else:    
        print(f'\nEl ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')

def juego_terminado(lista_de_intentos_ingresados, pal_adiv):
    '''
    Muestra en terminal la "Palabra a adivinar" y los intentos.
    '''
    print("Palabra a adivinar: ", end = "")
    mostrar_palabra(pal_adiv)
    for intento in lista_de_intentos_ingresados:
        mostrar_palabra(intento)

def mostrar_palabra(palabra_ingresada):
    '''
    Muestra por pantalla las palabras en el formato deseado.
    '''
    for letra in palabra_ingresada:
        print(letra + " " + obtener_color("Defecto"), end = "")
    print()

#PRINCIPAL
def fiuble():
    LONGITUD_PALABRAS = 5
    CANTIDAD_INTENTOS = 5
    jugar = ''
    usuarios_y_puntaje = ingreso_usuarios()#Diccionario: claves: nombres de usuario y valor: puntos acumulados
    turnos = orden_turnos(usuarios_y_puntaje)
    while jugar in ('s','S', ''):
        lista_de_intentos_ingresados = []
        pal_adiv = generar_palabra_a_adivinar()
        adivinar = crear_lista_interrogantes(LONGITUD_PALABRAS)
        palabras = crear_lista_intentos(CANTIDAD_INTENTOS, adivinar)
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(adivinar)
        for intento in palabras:
            mostrar_palabra(intento)
        print("Es el turno de:",turnos[0].upper())
        inicio = time.time()
        intento = input("Arriesgo:")
        intento = validacion_intento_ingresado(intento, lista_de_intentos_ingresados)
        lista_de_intentos_ingresados = desarrollo_intentos(pal_adiv, intento, turnos, adivinar, palabras) #Esta lista, es la lista de str de palabras ingresadas#
        fin = time.time()
        tiempo = cronometro(inicio, fin)
        if pal_adiv in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            print(f'Palabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos_ingresados,pal_adiv,usuarios_y_puntaje,turnos)
        jugar, turnos = volver_a_jugar(turnos)
    determinar_ganador(usuarios_y_puntaje)
fiuble()

