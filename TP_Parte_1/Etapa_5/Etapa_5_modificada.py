from utiles import *
import random
import time

'''Devuelve la palabra a adivinar en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.'''
def generar_palabra_a_adivinar():
    palabras_validas = obtener_palabras_validas()
    palabra=random.choice(palabras_validas)
    return palabra.upper()

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

'''
    Función: cambiar_tilde
    Parámetro:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin acentos.
'''
def cambiar_tilde(palabra_ingresada):
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = palabra_ingresada.maketrans(a, b)
    arriesgo = palabra_ingresada.translate(palabra_sin_acento)
    return arriesgo

'''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
        todos_turnos: para ir alternando los usuarios
    Salidas:
        Devuelve una lista con las palabras ingresadas.
'''
def desarrollo_intentos(pal_adiv, intento, turnos):
    #lista de listas, cada lista posee las letras de cada palabra ingresada
    palabras=[['?','?','?','?','?'],['?','?','?','?','?'],['?','?','?','?','?'],['?','?','?','?','?'],['?','?','?','?','?']]
    #lista que contendrá las letras de la palabra a adivinar cuando se dé un acierto en el intento
    adivinar=['?','?','?','?','?']
    #lista vacia que contendrá los intentos
    palabras_ingresadas=[]
    while len(palabras_ingresadas)<5 and pal_adiv not in palabras_ingresadas:
        orden_ingreso=len(palabras_ingresadas)
        #print(lista, palabras_ingresadas, orden_ingreso)
        for pos in range(len(pal_adiv)):
            if (pal_adiv.count(intento[pos])==1 and intento.count(intento[pos])==2):
                pos_1=intento.index(intento[pos])
                pos_2=intento.rindex(intento[pos])
                
                if ((pos==pos_1 and pos_1==pal_adiv.index(intento[pos_1])) or (pos==pos_2 and pos_2==pal_adiv.index(intento[pos_2]))):
                    color_1 = obtener_color("Verde")
                    #reemplazo el elemento lista[orden_ingreso][pos] por la letra pintada del intento
                    palabras[orden_ingreso][pos]=(color_1+intento[pos])
                    #corroboro que en la lista de la palabra a adivinar no se encuentra agregada la letra
                    if pal_adiv[pos] != adivinar[pos]:
                        #reemplazo '?' en la lista por la letra acertada
                        adivinar[pos]=pal_adiv[pos]
                                                           
                elif ((pos==pos_2 and pos_1==pal_adiv.index(intento[pos_1])) or (pos==pos_1 and pos_2==pal_adiv.index(intento[pos_2]))):
                    color_3 = obtener_color("GrisOscuro") 
                    palabras[orden_ingreso][pos]=(color_3+intento[pos])
                                                       
                elif (pos==pos_1 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                    color_2=obtener_color("Amarillo") 
                    palabras[orden_ingreso][pos]=(color_2+intento[pos])
                                        
                elif (pos==pos_2 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                    color_3 = obtener_color("GrisOscuro") 
                    palabras[orden_ingreso][pos]=(color_3+intento[pos])
                                        
            elif intento[pos] not in pal_adiv:
                color_3=obtener_color("GrisOscuro")
                palabras[orden_ingreso][pos]=(color_3+intento[pos])
                                
            elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
                color_2=obtener_color("Amarillo")
                palabras[orden_ingreso][pos]=(color_2+intento[pos])
                                
            elif intento[pos] == pal_adiv[pos]:
                color_1 = obtener_color("Verde") 
                palabras[orden_ingreso][pos]=(color_1+intento[pos])
                if pal_adiv[pos] != adivinar[pos]:
                    adivinar[pos]=pal_adiv[pos]
                                        
        print(f"\nPalabra a adivinar: {adivinar[0]} {adivinar[1]} {adivinar[2]} {adivinar[3]} {adivinar[4]}")
        for palabra in palabras:
            for letra in palabra:
                print(letra, obtener_color("Defecto"), end="")
            print()
            
        palabras_ingresadas = acumular_intentos(intento,palabras_ingresadas)
        if pal_adiv not in palabras_ingresadas and len(palabras_ingresadas)<5:
            print("Es el turno de:", turnos[len(palabras_ingresadas)].upper())
            arriesgo=input("Arriesgo:")
            intento=validacion(arriesgo)
    return palabras_ingresadas

'''
    Función: acumular_intentos
    Parámetros:
        palabra_ingresada: cadena de caracteres ingresado por el usuario.
        intentos_ingresados: lista vacia.
    Salidas:
        Devuelve la lista cargada con las palabras ingresadas.
'''
def acumular_intentos(palabra_ingresada,intentos_ingresados):
    intentos_ingresados.append(palabra_ingresada)
    return intentos_ingresados

'''
    Función: cronometro
    Parámetros:
        comienzo: inicia contador.
        final: detiene contador.
    Salidas:
        Devuelve los minutos y segundos tardados en finalizar el juego.
'''
def cronometro(comienzo, final):
    tiempo_tardado=(final-comienzo)
    if tiempo_tardado>=60:
        minutos=tiempo_tardado//60
        segundos=round(tiempo_tardado%60,0)
    else:
        minutos=0
        segundos=round(tiempo_tardado,0)
    return minutos, segundos

'''
    Función: puntaje
    Parámetros:
        lista: lista de cadenas de caracteres.
        adivinar: cadena de caracteres, palabra a adivinar.
        todos_turnos: lista vacia.
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
'''
def puntaje(lista,adivinar,usuarios,turnos):
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

''' Funcion que acumula el puntaje para cada jugador.'''
def contador_puntajes (puntos_obtenidos,usuarios,turnos,indice):
    jugador_acierto = turnos[indice]
    jugador_fallo = turnos[indice-1]
    usuarios[jugador_acierto] += puntos_obtenidos
    if puntos_obtenidos > 0:
        usuarios[jugador_fallo] += -puntos_obtenidos
        print(f"{jugador_acierto.upper()}, ha ganado: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_acierto]} puntos.")
        print(f"{jugador_fallo.upper()}, ha perdido: {puntos_obtenidos} puntos. Tiene acumulados {usuarios[jugador_fallo]} puntos.")
    print(f"Puntajes parciales: {usuarios}")
    return usuarios

'''Devuelve la respuesta de seguir jugando, de ser afirmativa devuelve el nuevo orden de los turnos.''' 
def volver_a_jugar(turnos):
    desea_jugar = input("¿Desea volver a jugar?(S/N):")
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input("¿Desea volver a jugar?(S/N):")
    if desea_jugar in ('s','S'):
        turnos = nueva_partida(turnos)
    return  desea_jugar, turnos

''' Carga un diccionario, las claves son los ususarios y el valor acumulara sus respectivos puntajes.'''
def ingreso_usuarios():
    usuarios = {}
    usuario_1 = input("Ingreso usuario:")
    usuario_2 = input("Ingreso usuario:")
    usuarios[usuario_1] = 0
    usuarios[usuario_2] = 0
    return usuarios

''' Generador de turnos '''
def orden_turnos (usuarios):
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

''' Función que va alternando los turnos partida a partida'''
def nueva_partida(orden_jugador):
    orden_jugador.append(orden_jugador[1])
    del(orden_jugador[0])
    return orden_jugador

def determinar_ganador(usuarios):
    orden =sorted(usuarios.items(), key=lambda x:x[1], reverse=True)
    print(f'\nEl ganador es {orden[0][0].upper()} con un total de {orden[0][1]} puntos.')
    
#PRINCIPAL
def fiuble():
    partida=0
    jugar=''
    usuarios_y_puntaje=ingreso_usuarios()#Diccionario: claves: nombres de usuario y valor: puntos acumulados
    turnos= orden_turnos(usuarios_y_puntaje)
    while (partida==0 and jugar=='') or jugar in ('s','S'):
        pal_adiv=generar_palabra_a_adivinar()
        print("Palabra a adivinar: ? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?")
        print("Es el turno de:",turnos[0].upper())
        inicio=time.time()
        intento=input("Arriesgo:")
        intento=validacion(intento)
        lista_de_intentos_ingresados=desarrollo_intentos(pal_adiv, intento, turnos) #Esta lista, es la lista de str de palabras ingresadas#
        fin=time.time()
        minutos,segundos=cronometro(inicio, fin)
        if pal_adiv in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',minutos,'minutos y',segundos,'segundos')
        else:
            print(f'Palabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]} {obtener_color("Defecto")}\nPerdiste!')
        puntaje(lista_de_intentos_ingresados,pal_adiv,usuarios_y_puntaje,turnos)
        jugar, turnos = volver_a_jugar(turnos)
    determinar_ganador(usuarios_y_puntaje)
fiuble()
