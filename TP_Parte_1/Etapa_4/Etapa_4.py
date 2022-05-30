from utiles import *
import random
import time
#ETAPA 3
'''Devuelve la palabra a adivinar en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.'''
def generar_palabra_a_adivinar():
    palabras_validas = obtener_palabras_validas()
    palabra=random.choice(palabras_validas)
    return palabra.upper()

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
        Devuelve la palabra sin acentos.
'''
def cambiar_tilde(palabra_ingresada):
    a = 'áéíóúýäëïöüÿàèìòùâêîôû'
    b = 'aeiouyaeiouyaeiouaeiou'
    palabra_sin_acento = palabra_ingresada.maketrans(a, b)
    arriesgo = palabra_ingresada.translate(palabra_sin_acento)
    return arriesgo

#ETAPA 1 ADAPTADA A 3
'''
    Función: desarrollo_intentos
    Parámetros:
        pal_adiv: palabra a adivinar.
        intento: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve una lista con las palabras ingresadas.
'''
def desarrollo_intentos(pal_adiv, intento):
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
            arriesgo=input("Arriesgo:")
            intento=validacion(arriesgo)
    return palabras_ingresadas

#ETAPA 3
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

#ETAPA 4
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
        puntos_por_partida: lista vacia.
    Salidas:
        Devuelve la lista cargada con el puntaje obtenido una vez finalizada la partida.
'''
def puntaje(lista,adivinar,puntos_por_partida):
    valores=[50,40,30,20,10,-100]
    if adivinar not in lista and len(lista)==5:
        puntos_obtenidos=-100
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
    return almacenamiento_puntos(puntos_obtenidos,puntos_por_partida)

'''
    Función: almacenamiento_puntos
    Parámetros:
        puntos_obtenidos: puntaje de la partida
        puntos_por partida: lista vacia
    Salida:
        Devuelve la lista cargada con el puntaje.
'''
def almacenamiento_puntos(puntos_obtenidos,puntos_por_partida):
    puntos_por_partida.append(puntos_obtenidos)
    return puntos_por_partida

'''
    Función: contador_puntos
    Parámetros:
        puntos_por_partida: lista cargada con los puntos de las partidas.
    Salida:
        Imprime los puntos obtenidos en la partida y el total de puntos acumulados por el usuario.
'''
def contador_puntos(puntos_por_partida):
    total = 0
    ultima_partida=puntos_por_partida[-1]
    if len(puntos_por_partida) > 1:
        for puntajes in puntos_por_partida:
            total += puntajes
        if ultima_partida>0:
            print(f'Obtuviste un total de {ultima_partida} puntos, tenes acumulados {total} puntos')
        else:
            print(f'Perdiste un total de {-ultima_partida} puntos, tenes acumulados {total} puntos')
    else:
        if ultima_partida>0:
            print(f'Obtuviste un total de {ultima_partida} puntos.')
        else:
            print(f'Perdiste un total de {-ultima_partida} puntos.')

'''Devuelve la respuesta de seguir jugando.'''
def volver_a_jugar():
    desea_jugar = input("¿Desea volver a jugar?(S/N):")
    while desea_jugar not in ('N','n','s','S'):
        desea_jugar = input("¿Desea volver a jugar?(S/N):")
    return  desea_jugar

#PRINCIPAL
def fiuble():
    puntos_por_partida=[] #Lista de puntos de cada partida#
    partida=0
    jugar=''
    while (partida==0 and jugar=='') or jugar in ('s','S'):
        pal_adiv=generar_palabra_a_adivinar()
        print("Palabra a adivinar: ? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?")
        inicio=time.time()
        intento=input("Arriesgo:")
        intento=validacion(intento)
#        color_4=obtener_color("Defecto")
        lista_de_intentos_ingresados=desarrollo_intentos(pal_adiv, intento) #Esta lista, es la lista de str de palabras ingresadas#
        fin=time.time()
        puntos_obtenidos=puntaje(lista_de_intentos_ingresados,pal_adiv,puntos_por_partida) #Lista cargada de puntos obtenidos por partida#
        minutos,segundos=cronometro(inicio, fin)
        if pal_adiv in lista_de_intentos_ingresados:
            print('Ganaste! Tardaste',minutos,'minutos y',segundos,'segundos')
        else:
            print(f'Palabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]} {obtener_color("Defecto")}\nPerdiste!')
        contador_puntos(puntos_obtenidos)
        jugar = volver_a_jugar()
fiuble()
