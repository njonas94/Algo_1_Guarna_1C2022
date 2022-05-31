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
    palabra_adivinar=random.choice(palabras_validas)

    return palabra_adivinar.upper()

def validacion_intento_ingresado(intento_pre_validacion, lista_de_intentos):
    '''
    Función: validar_intento_ingresado
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    intento_pre_validacion_sin_tildes = cambiar_tilde(intento_pre_validacion.lower())
    while not intento_pre_validacion_sin_tildes.isalpha() or intento_pre_validacion_sin_tildes.lower() not in obtener_palabras_validas() or intento_pre_validacion_sin_tildes.upper() in lista_de_intentos:
        if not intento_pre_validacion_sin_tildes.isalpha() and len(intento_pre_validacion_sin_tildes) != 5:
            print("Palabra inválida, tiene que ser de 5 letras y no puede contener número/s ni caracteres especiales.")
        elif len(intento_pre_validacion_sin_tildes) != 5:
            print("Palabra inválida, tiene que ser de 5 letras.")
        elif intento_pre_validacion_sin_tildes not in obtener_palabras_validas() and intento_pre_validacion_sin_tildes.isalpha():
            print("Palabra inválida.")
        elif intento_pre_validacion_sin_tildes.upper() in lista_de_intentos:
            print("La palabra ya habia sido ingresada.")
        else:#if not palabra_ingresada.isalpha():
            print("Palabra inválida, no puede contener números ni caracteres especiales.")
        intento_pre_validacion = input("Ingrese una palabra valida de 5 letras: ")
        intento_pre_validacion_sin_tildes = cambiar_tilde(intento_pre_validacion.lower())
    intento = intento_pre_validacion_sin_tildes 
    return intento.upper()

def cambiar_tilde(intento_pre_validacion):
    '''
    Función: cambiar_tilde
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin acentos.
    '''
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = intento_pre_validacion.maketrans(a, b)
    intento_pre_validacion_sin_tildes = intento_pre_validacion.translate(palabra_sin_acento)
    
    return intento_pre_validacion_sin_tildes

def crear_lista_palabra_adivinar(LONGITUD_PALABRAS):
    '''
    Autor : Aldair Torres
    Pre: recibe la palabra a adivinar para saber su longitud
    Post: Nos devuelve una lista conformada por signos de interrogacion
    '''
    lista_palabra_adivinar = []
    for i in range(LONGITUD_PALABRAS):
        lista_palabra_adivinar.append('?')
    
    return lista_palabra_adivinar

def crear_lista_de_listas_de_intentos(CANTIDAD_INTENTOS, lista_palabra_adivinar):
    '''
    Autor: Aldair Torres
    Pre: recibe una cantidad de intentos y una lista con interrogantes
    Post: Nos devuelve una lista de listas en donde se almacenas los intentos
    '''
    lista_de_listas_de_intentos = []
    for i in range(CANTIDAD_INTENTOS):
        lista_de_listas_de_intentos.append(lista_palabra_adivinar.copy())
    
    return lista_de_listas_de_intentos

def procesar_intento(palabra_adivinar, intento, lista_palabra_adivinar):
    '''
    Procesa el intento ingresado, creando una lista con el correspondiente color asignado a cada letra en el mismo indice que el string ingresado.
    '''
    colores = []
    for pos in range(len(palabra_adivinar)):
        if (palabra_adivinar.count(intento[pos]) == 1 and intento.count(intento[pos]) == 2):
            pos_1 = intento.index(intento[pos])
            pos_2 = intento.rindex(intento[pos])

            if ((pos == pos_1 and pos_1 == palabra_adivinar.index(intento[pos_1])) or (
                    pos == pos_2 and pos_2 == palabra_adivinar.index(intento[pos_2]))):
                colores.append(obtener_color("Verde"))
                lista_palabra_adivinar[pos] = palabra_adivinar[pos]

            elif ((pos == pos_2 and pos_1 == palabra_adivinar.index(intento[pos_1])) or (
                    pos == pos_1 and pos_2 == palabra_adivinar.index(intento[pos_2]))):
                colores.append(obtener_color("GrisOscuro"))

            elif (pos == pos_1 and pos_1 != palabra_adivinar.index(intento[pos_1]) and pos_2 != palabra_adivinar.index(intento[pos_1])):
                colores.append(obtener_color("Amarillo"))

            elif (pos == pos_2 and pos_1 != palabra_adivinar.index(intento[pos_1]) and pos_2 != palabra_adivinar.index(intento[pos_1])):
                colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] not in palabra_adivinar:
            colores.append(obtener_color("GrisOscuro"))

        elif intento[pos] in palabra_adivinar and intento[pos] != palabra_adivinar[pos]:
            colores.append(obtener_color("Amarillo"))

        elif intento[pos] == palabra_adivinar[pos]:
            colores.append(obtener_color("Verde"))
            lista_palabra_adivinar[pos] = palabra_adivinar[pos]

    return colores

def desarrollo_intentos(palabra_adivinar, intento, turnos, lista_palabra_adivinar, lista_de_listas_de_intentos):
    '''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
        todos_turnos: para ir alternando los usuarios
    Salidas:
        Devuelve una lista con las palabras ingresadas.
    '''
    lista_de_intentos=[]
    while len(lista_de_intentos)<5:
        orden_ingreso=len(lista_de_intentos)
        #print(lista, palabras_ingresadas, orden_ingreso)
        colores = procesar_intento(palabra_adivinar, intento, lista_palabra_adivinar)
        acumular_intentos(intento, orden_ingreso, colores, lista_de_listas_de_intentos, lista_de_intentos)
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(lista_palabra_adivinar)
        for intento in lista_de_listas_de_intentos:
            mostrar_palabra(intento)
            
        if palabra_adivinar not in lista_de_intentos and len(lista_de_intentos)<5:
            print("Es el turno de:", turnos[len(lista_de_intentos)].upper())
            intento_pre_validacion=input("Arriesgo:")
            intento=validacion_intento_ingresado(intento_pre_validacion, lista_de_intentos)
   
    return lista_de_intentos

def acumular_intentos(intento, orden_ingreso, colores, lista_de_listas_de_intentos, lista_de_intentos):
    '''
    Función: acumular_intentos
    Acumula los intentos ingresados en una lista, con el respectivo color de letra correspondiente asociado.
    Parámetros:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        intentos_ingresados: lista vacia.
    Salidas:
        Devuelve la lista cargada con las palabras ingresadas.
    '''
    lista_de_intentos.append(intento)
    for i in range(len(intento)):
        lista_de_listas_de_intentos[orden_ingreso][i] = colores[i] + intento[i]

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

def puntaje(lista_de_intentos_ingresados,palabra_adivinar,usuarios_y_puntaje,turnos):
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
    if palabra_adivinar not in lista_de_intentos_ingresados and len(lista_de_intentos_ingresados)==5:
        usuarios_y_puntaje[turnos[0]]+= valores[-1]
        usuarios_y_puntaje[turnos[1]]+= valores[-2]
        print(f"{turnos[0].upper()}, ha perdido, 100 puntos. Tiene acumulados {usuarios_y_puntaje[turnos[0]]} puntos.")
        print(f"{turnos[1].upper()}, ha perdido, 50 puntos. Tiene acumulados {usuarios_y_puntaje[turnos[1]]} puntos.")
    elif palabra_adivinar in lista_de_intentos_ingresados:
        if len(lista_de_intentos_ingresados)==1:
            puntos_obtenidos=valores[0]
        elif len(lista_de_intentos_ingresados)==2:
            puntos_obtenidos=valores[1]
        elif len(lista_de_intentos_ingresados)==3:
            puntos_obtenidos=valores[2]
        elif len(lista_de_intentos_ingresados)==4:
            puntos_obtenidos=valores[3]
        elif len(lista_de_intentos_ingresados)==5:
            puntos_obtenidos=valores[4]
        indice = len(lista_de_intentos_ingresados)-1
        usuarios_y_puntaje = contador_puntajes (puntos_obtenidos,usuarios_y_puntaje,turnos,indice)
    
    return usuarios_y_puntaje

def contador_puntajes (puntos_obtenidos,usuarios_y_puntaje,turnos,indice):
    ''' 
    Funcion que acumula el puntaje para cada jugador.
    '''
    jugador_acierto = turnos[indice]
    if indice ==0:
        jugador_fallo = turnos[indice-2]
    else:
        jugador_fallo = turnos[indice-1]
    usuarios_y_puntaje[jugador_acierto] += puntos_obtenidos
    if puntos_obtenidos > 0:
        usuarios_y_puntaje[jugador_fallo] += -puntos_obtenidos
        print(f"{jugador_acierto.upper()}, ha ganado: {puntos_obtenidos} puntos. Tiene acumulados {usuarios_y_puntaje[jugador_acierto]} puntos.")
        print(f"{jugador_fallo.upper()}, ha perdido: {puntos_obtenidos} puntos. Tiene acumulados {usuarios_y_puntaje[jugador_fallo]} puntos.")
    
    return usuarios_y_puntaje
 
def volver_a_jugar(turnos):
    '''
    Devuelve la respuesta de seguir jugando, de ser afirmativa devuelve el nuevo orden de los turnos.
    '''
    desea_jugar = input("\n¿Desea volver a jugar?(S/N):")
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input("¿Desea volver a jugar?(S/N):")
    if desea_jugar in ('s','S'):
        turnos = turnos_nueva_partida(turnos)
    
    return  desea_jugar, turnos

def ingreso_usuarios():
    ''' 
    Carga un diccionario, las claves son los ususarios y el valor acumulara sus respectivos puntajes.
    '''
    usuarios_y_puntaje = {}
    usuario_1 = input("Ingreso usuario:")
    usuario_2 = input("Ingreso usuario:")
    usuarios_y_puntaje[usuario_1] = 0
    usuarios_y_puntaje[usuario_2] = 0
    
    return usuarios_y_puntaje

def orden_turnos (usuarios_y_puntaje):
    ''' 
    Generador de turnos 
    '''
    turnos = []
    nombre = list(usuarios_y_puntaje.keys())
    master=random.choice(nombre)
    indice = nombre.index(master)
    for i in range(5):
        if i in (0,2,4):
            turnos.append(master)              
        else:
            turnos.append(nombre[indice-1])
    
    return turnos

def turnos_nueva_partida(turnos):
    ''' 
    Función que va alternando los turnos partida a partida
    '''
    turnos.append(turnos[1])
    del(turnos[0])
    
    return turnos

def determinar_ganador(usuarios_y_puntaje):
    orden =sorted(usuarios_y_puntaje.items(), key=lambda x:x[1], reverse=True)
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
        lista_de_intentos = []
        palabra_adivinar = generar_palabra_a_adivinar()
        lista_palabra_adivinar = crear_lista_palabra_adivinar(LONGITUD_PALABRAS)
        lista_de_listas_de_intentos = crear_lista_de_listas_de_intentos(CANTIDAD_INTENTOS, lista_palabra_adivinar)
        print("Palabra a adivinar: ", end = "")
        mostrar_palabra(lista_palabra_adivinar)
        for intento in lista_de_listas_de_intentos:
            mostrar_palabra(intento)
        print("Es el turno de:",turnos[0].upper())
        inicio = time.time()
        intento_pre_validacion = input("Arriesgo:")
        intento = validacion_intento_ingresado(intento_pre_validacion, lista_de_intentos)
        lista_de_intentos = desarrollo_intentos(palabra_adivinar, intento, turnos, lista_palabra_adivinar, lista_de_listas_de_intentos) #Esta lista, es la lista de str de palabras ingresadas#
        fin = time.time()
        tiempo = cronometro(inicio, fin)
        if palabra_adivinar in lista_de_intentos:
            print('Ganaste! Tardaste',tiempo[0],'minutos y',tiempo[1],'segundos')
        else:
            print(f'Palabra a adivinar: {palabra_adivinar[0]} {palabra_adivinar[1]} {palabra_adivinar[2]} {palabra_adivinar[3]} {palabra_adivinar[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos,palabra_adivinar,usuarios_y_puntaje,turnos)
        jugar, turnos = volver_a_jugar(turnos)
    determinar_ganador(usuarios_y_puntaje)
fiuble()
