from interfaz_usuario import *
from procesar_archivos import *

def impresion(variable,valor,datos,info):
    default=['7','5','False']
    if variable!='' and valor=='':
        print('{}: {} y fue asignada por omisión'.format(variable, valor))
        datos.append(default[info])
    elif valor!='' and variable!='':
        print('{}: {} y fue asignada por configuración'.format(variable, valor))
        datos.append(valor)
    return datos

def leer_configuracion ():
    datos=[]
    lista_final=[]
    info=0
    archivo = open("configuracion.csv", "r")
    variable, valor= leer_archivo(archivo,',')
    while (variable!='' and valor=='') or (variable!='' and valor!='' ):
        lista=impresion(variable,valor,datos,info)
        variable, valor= leer_archivo(archivo,',')
        if lista[info].isdigit():
            lista_final.append(int(lista[info]))
        else:
            lista_final.append(bool(lista[info]))
        info+=1

    return lista_final
