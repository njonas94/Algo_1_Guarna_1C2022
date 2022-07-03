import re
import os
import pandas as pd
import csv


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
    for linea in archivo:
        if linea:
            linea = re.sub(r'[^\w\s]', '', linea)
            linea = linea.rstrip("\n").split()
            for palabra in linea:
                if not palabra.isalpha():
                    linea.remove(palabra)


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
