from interfaz_usuario import *
from procesar_archivos import *


def impresion(parametro, valor_parametro, lista_datos, contador):
    '''
    Función: impresion
    Descripción:
        Asigna valores Defaults o por Configuración a una lista.
    Parametros:
        Parametro: String proveniente del archivo.
        valor_parametro: valor del parametro proveniente del archivo.
        lista_datos: Lista de datos sobre la partida
        contador: Entero que funciona como contador.
    Salida:
        Retorna lista con los valores agregados.
    '''
    lista_default = ['7', '5', 'False']
    if parametro != '' and valor_parametro == '':
        print('{}: {} y fue asignada por omisión'.format(parametro, valor_parametro))
        lista_datos.append(lista_default[contador])
    elif valor_parametro != '' and parametro != '':
        print('{}: {} y fue asignada por configuración'.format(parametro, valor_parametro))
        lista_datos.append(valor_parametro)
    return lista_datos


def leer_configuracion():
    '''
    Función: leer_configuracion
    Descripción:
        Lee un archivo y agrega los valores del archivo/defaults a una lista.
    Salida:
        lista_final: Lista con los valores agregados.
    '''
    lista_datos = []
    lista_final_datos = []
    contador = 0
    archivo = open("configuracion.csv", "r")
    parametro, valor_parametro = leer_archivo(archivo, ',')
    while (parametro != '' and valor_parametro == '') or (parametro != '' and valor_parametro != ''):
        lista = impresion(parametro, valor_parametro, lista_datos, contador)
        parametro, valor_parametro = leer_archivo(archivo, ',')
        if lista[contador].isdigit():
            lista_final_datos.append(int(lista[contador]))
        elif lista[contador] == 'False':
            lista_final_datos.append(False)
        else:
            lista_final_datos.append(bool(lista[contador]))
        contador += 1

    return lista_final_datos
