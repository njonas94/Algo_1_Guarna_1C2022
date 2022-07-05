import os
import pandas as pd
import csv
from utiles import *

def leer_archivos_texto(archivo):
    """
    Funcion: leer_archivo_texto
    Descripcion:
        Va leyendo el texto, elimina los signos que se encuentren en la palabra (¿?¡!-_.:,;) y los
        elimina si no son alpha
    Parametro:
        archivo: Texto a leer
    Salida:
        No se como quiere recibir la persona que necesita esta funcion
    """
    linea = archivo.readline()
    return linea

def ordenar_archivo_partidas(nombre_archivo):
    """
    Funcion: ordenar:archivo_partidas
    Descripcion:
        Lee el archivo, lo ordena de forma descendente y despues lo pasa al archivo csv
    Parametros:
        nombre_archivo: nombre del archivo que se va a ordenar
    """
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    archivo = pd.read_csv(nombre_archivo)
    archivo_ordenado = archivo.sort_values(by = ['Aciertos'], ascending = [False])
    archivo_ordenado.to_csv(nombre_archivo, header = lista_encabezado, index = False)


def crear_archivo_partidas(nombre_archivo, dicc_datos):
    """
    Funcion: crear_archivo_partidas
    Descripcion:
        Crea el archivo con encabezado y escribe las primeras lineas
    Parametros:
        nombre_archivo: nombre para el archivo a crear
        dicc_datos: diccionario con los datos extraidos de la partida
    """
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    with open(nombre_archivo, 'w', newline='') as archivo_partidas:
        archivo = csv.DictWriter(archivo_partidas, fieldnames = lista_encabezado)
        archivo.writeheader()
        archivo.writerow(dicc_datos)


def escribir_archivo_partidas(nombre_archivo, dicc_datos):
    """
    Funcion: escribir_archivo_partidas
    Descripcion:
        Añade una linea con los datos de la partida
    Parametros:
        nombre_archivo: nombre del archivo a escribir
        dicc_datos: diccionario con los datos extraidos de la partida
    """
    # Si tengo q pasar de dos jugadores, tengo que usar el writerows[dicc1, dicc2]
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    with open(nombre_archivo, 'a', newline='') as archivo_partidas:
        archivo = csv.DictWriter(archivo_partidas, fieldnames = lista_encabezado)
        archivo.writerow(dicc_datos)


def registro_partidas(dicc_datos):
    """
    Funcion: registro_partidas
    Descripcion:
        Determina si el archivo partidas.csv existe, para escribirlo o crearlo
    Parametros:
        dicc_datos: diccionario con los datos extraidos de la partida
    """
    nombre_archivo = 'partidas.csv'
    if not os.path.isfile(nombre_archivo):
        crear_archivo_partidas(nombre_archivo, dicc_datos)
    else:
        escribir_archivo_partidas(nombre_archivo, dicc_datos)

def procesar_linea(lista_linea, LONGITUD_PALABRAS):
    """
    Funcion: procesar_linea
    Descripcion:
        Determina si el archivo partidas.csv existe, para escribirlo o crearlo
    Parametros:
        lista_linea: lista generada con las palabras en una linea leida de un archivo.
        LONGITUD_PALABRAS: entero con la longitud de las palabras para jugar
    Salida:
        Devuelve una nueva lista, solo con las palabras de longitud deseada, sin caracteres especiales y en minuscula.
    """
    caracteres_especiales = '''_-.,¡!¿?$%#/<>:;«»"()[]1234567890'''
    lista_palabras = []

    lista_linea = lista_linea.rstrip('\n').split(" ")

    for indice in range(len(lista_linea)):
        for caracter in caracteres_especiales:
            lista_linea[indice] = lista_linea[indice].replace(caracter,"")

        lista_linea[indice] = cambiar_tilde(lista_linea[indice])
        lista_linea[indice] = lista_linea[indice].lower()

    for palabra in lista_linea:
        if len(palabra) == LONGITUD_PALABRAS:
            lista_palabras.append(palabra)

    return lista_palabras

def cargar_diccionario(diccionario, lista_palabras, numero_archivo):
    """
    Funcion: cargar_diccionario
    Descripcion:
        Determina si el archivo partidas.csv existe, para escribirlo o crearlo
    Parametros:
        diccionario: diccionario con las palabras y el contador por archivo.
        lista_palabras: lista con las palabras de longitud deseada, sin caracteres especiales y en minuscula.
        numero_archivo: Entero identificador del archivo que se esta leyendo.
    """
    for palabra in lista_palabras:
        if palabra in diccionario:
            diccionario[palabra][numero_archivo] += 1

        else:
            diccionario[palabra] = [0,0,0]
            diccionario[palabra][numero_archivo] += 1


def palabras_validas(archivo0, archivo1, archivo2, diccionario_palabras_validas, LONGITUD_PALABRAS):
    """
    Funcion: palabras_validas
    Descripcion:
        Determina si el archivo partidas.csv existe, para escribirlo o crearlo
    Parametros:
        archivo0: 1er archivo abierto.
        archivo1: 2do archivo abierto.
        archivo2: 3er archivo abierto.
        diccionario_palabras_validas: diccionario con las palabras y el contador por archivo.
    """
    linea0 = leer_archivos_texto(archivo0)
    linea1 = leer_archivos_texto(archivo1)
    linea2 = leer_archivos_texto(archivo2)

    while linea0:
        lista0 = procesar_linea(linea0, LONGITUD_PALABRAS)
        cargar_diccionario(diccionario_palabras_validas, lista0, 0)
        linea0 = leer_archivos_texto(archivo0)

    while linea1:
        lista1 = procesar_linea(linea1, LONGITUD_PALABRAS)
        cargar_diccionario(diccionario_palabras_validas, lista1, 1)
        linea1 = leer_archivos_texto(archivo1)

    while linea2:
        lista2 = procesar_linea(linea2, LONGITUD_PALABRAS)
        cargar_diccionario(diccionario_palabras_validas, lista2, 2)
        linea2 = leer_archivos_texto(archivo2)


def archivo_palabras(lista_ordenada):
    archivo = open("palabras.csv","w")
    for palabra in lista_ordenada:
        archivo.write(palabra[0] + "," + str(palabra[1][0]) + "," + str(palabra[1][1]) + "," + str(palabra[1][2]) + "\n")
    archivo.close()

def ordenar_diccionario(diccionario_palabras):
    lista_ordenada = sorted(diccionario_palabras.items(), key=lambda x: x[0])
    
    return lista_ordenada

def escribir_archivo_palabras(lista_ordenada):
    archivo = open("palabras.csv","w")
    for palabra in lista_ordenada:
        archivo.write(palabra[0] + "," + str(palabra[1]) + "," + str(palabra[2]) + "," + str(palabra[3]) + "\n")
    archivo.close()

def ordenar_diccionario(diccionario_palabras):
    lista_ordenada = sorted(diccionario_palabras.items(), key=lambda x: x[0])
    escribir_archivo_palabras(lista_ordenada)

def leer_archivo(archivo, default):
    linea=archivo.readline()
    if linea:
        lista=linea.rstrip('\n').split(',')
    else:
        lista=default.split(',')    
    return lista

def crear_diccionario_usuarios_datos(turnos):
    '''
    Función: crear_diccionario_usuarios_datos
    Descripción:
        Crea el diccionario con los usuarios correspondientes como clave y 3er valor.
    Parametros:
        turnos: Lista de turnos.
    Salida:
        Retorna diccionario creado con los nombres de usuarios cargados.
    '''
    usuarios_datos = {}
    usuarios_datos[turnos[0]] = ['','','',0,0]
    usuarios_datos[turnos[0]][-3] = turnos[0]
    usuarios_datos[turnos[1]] = ['','','',0,0]
    usuarios_datos[turnos[1]][-3] = turnos[1]
    return usuarios_datos

def cargar_hora(turnos,fecha,hora,usuarios_datos):
    '''
    Función: cargar_hora
    Descripción:
        Cargar la fecha/hora en el diccionario que recibe como parametro.
    Parametros:
        turnos: Lista de turnos.
        fecha:  String con la fecha.
        hora: String con la hora.
        usuarios_datos: Diccionario con los usuarios.
    Salida:
        Retorna diccionario con los datos fecha/hora cargados.
    '''
    lista_jugadores=[turnos[0],turnos[1]]
    for jugador in lista_jugadores:
        usuarios_datos[jugador][0]=fecha
        usuarios_datos[jugador][1]=hora
    return usuarios_datos


def cargar_aciertos_e_intentos(lista_de_intentos_ingresados, palabra_adivinar, usuarios_datos, turnos):
    '''
    Función: cargar_aciertos_e_intentos
    Descripción:
        Agrega los intentos/aciertos correspondientes al diccionario usuarios_datos.
    Parametros:
        lista_de_intentos_ingresados: Lista de intentos ingresados.
        palabra_adivinar: String palabra a adivinar.
        usuarios_datos: Diccionario con los usuarios.
        turnos: Lista de turnos.
    Salida:
        Retora lista de listas con los valores de los usuarios en el diccionario que recibe como parametro.    
    '''    
    if palabra_adivinar not in lista_de_intentos_ingresados and len(lista_de_intentos_ingresados)==5:
        usuarios_datos[turnos[0]][-1]+=3
        usuarios_datos[turnos[1]][-1]+=2

    elif palabra_adivinar in lista_de_intentos_ingresados:
        indice = len(lista_de_intentos_ingresados)-1
        
        jugador_acierto = turnos[indice]
        if indice ==0:
            jugador_fallo = turnos[indice-2]
        else:
            jugador_fallo = turnos[indice-1]
        
        if len(lista_de_intentos_ingresados)==1:
            usuarios_datos[jugador_acierto][-1]+=1
            usuarios_datos[jugador_acierto][-2]+=1
            
        elif len(lista_de_intentos_ingresados)==2:
            usuarios_datos[jugador_acierto][-1]+=1
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=1
            
        elif len(lista_de_intentos_ingresados)==3:
            usuarios_datos[jugador_acierto][-1]+= 2
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=1
            
        elif len(lista_de_intentos_ingresados)==4:
            usuarios_datos[jugador_acierto][-1]+=2
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=2
           
            
        elif len(lista_de_intentos_ingresados)==5:
            usuarios_datos[jugador_acierto][-1]+=3
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=2               
    return usuarios_datos.values()
    
    
def limpiar_archivo(REINICIAR_PARTIDAS_CSV):
    '''
    Función: limpiar_archivo
    Descripcion:
        Resetear el archivo partidas.csv al final del juego en caso que asi se indique.
    Parametro:
        REINICIAR_PARTIDAS_CSV: Variable booleana del archivo configuración.
    '''
    if REINICIAR_PARTIDAS_CSV:
        reinicio = open("partidas.csv","w")
        reinicio.close()
    return


""" 
Pruebas de las funciones para ver si andan bien
leer_archivos_texto(archivo = open('cuentos.txt', 'r'))
dicc1 = {'Fecha partida': '231232', 'Hora finalizacion': '123412', 'Jugador': 'alda', 'Aciertos': 20, 'Intentos': 2}
dicc2 = {'Fecha partida': '122211', 'Hora finalizacion': '112435', 'Jugador': 'eze', 'Aciertos': 31, 'Intentos': 8}
dicc3 = {'Fecha partida': '112341', 'Hora finalizacion': '032312', 'Jugador': 'feli', 'Aciertos': 4, 'Intentos': 5}
dicc4 = {'Fecha partida': '045635', 'Hora finalizacion': '231211', 'Jugador': 'jorge', 'Aciertos': 13, 'Intentos': 3}

registro_partidas(dicc1)
registro_partidas(dicc2)
registro_partidas(dicc3)
registro_partidas(dicc4)
ordenar_archivo_partidas('partidas.csv')
"""
