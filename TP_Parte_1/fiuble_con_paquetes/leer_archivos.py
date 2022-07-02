import re
import os
import pandas as pd
import csv


def leer_archivos(archivo):
    for linea in archivo:
        if linea:
            linea = re.sub(r'[^\w\s]', '', linea)
            linea = linea.rstrip("\n").split()
            for palabra in linea:
                if not palabra.isalpha():
                    linea.remove(palabra)

                    
def ordenar_archivo_partidas(nombre_archivo):
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    archivo = pd.read_csv(nombre_archivo)
    archivo_ordenado = archivo.sort_values(by = ['Aciertos'], ascending = [False])
    archivo_ordenado.to_csv(nombre_archivo, header = lista_encabezado)


def crear_archivo_partidas(nombre_archivo, dicc_datos):
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    with open(nombre_archivo, 'w', newline='') as archivo_partidas:
        archivo = csv.DictWriter(archivo_partidas, fieldnames = lista_encabezado)
        archivo.writeheader()
        archivo.writerow(dicc_datos)


def escribir_archivo_partidas(nombre_archivo, dicc_datos):
    # Si tengo q pasar de dos jugadores, tengo que usar el writerows[dicc1, dicc2]
    lista_encabezado = ['Fecha partida', 'Hora finalizacion', 'Jugador', 'Aciertos', 'Intentos']
    with open(nombre_archivo, 'a', newline='') as archivo_partidas:
        archivo = csv.DictWriter(archivo_partidas, fieldnames = lista_encabezado)
        archivo.writerow(dicc_datos)


def registro_partidas(dicc_datos):
    nombre_archivo = 'partidas.csv'
    if not os.path.isfile(nombre_archivo):
        crear_archivo_partidas(nombre_archivo, dicc_datos)
    else:
        escribir_archivo_partidas(nombre_archivo, dicc_datos)


# leer_archivos(archivo = open('cuentos.txt', 'r'))
dicc1 = {'Fecha partida': '231232', 'Hora finalizacion': '123412', 'Jugador': 'alda', 'Aciertos': 23, 'Intentos': 2}
dicc2 = {'Fecha partida': '122211', 'Hora finalizacion': '112435', 'Jugador': 'eze', 'Aciertos': 5, 'Intentos': 8}
dicc3 = {'Fecha partida': '112341', 'Hora finalizacion': '032312', 'Jugador': 'feli', 'Aciertos': 10, 'Intentos': 5}
dicc4 = {'Fecha partida': '045635', 'Hora finalizacion': '231211', 'Jugador': 'jorge', 'Aciertos': 1, 'Intentos': 3}

registro_partidas(dicc1)
registro_partidas(dicc2)
registro_partidas(dicc3)
registro_partidas(dicc4)
ordenar_archivo_partidas('partidas.csv')
