from interfaz_usuario import *

def mostrar_palabra(palabra_ingresada):
    '''
    Función: mostrar_palabra
    Descripción: 
        Recibe una palabra y la muestra en el formato deseado.
    Parametro:
        palabra_ingresada: Palabra que segun el momento de su ejecución varía.    
    '''
    for letra in palabra_ingresada:
        print(letra + ' ' + obtener_color('Defecto'), end = '')
    print() 

def mostrar_palabra_adivinar(palabra_a_adivinar):
    '''
    Función: mostrar_palabra_adivinar
    Descripción: 
        Recibe una palabra y la muestra en el formato deseado.
    Parametro:
        palabra_a_adivinar: Palabra a adivinar, que se mostrará al terminar la partida.    
    '''
    print("Palabra a adivinar: ", end = "")
    for i in range(len(palabra_a_adivinar)):
        print(f"{palabra_a_adivinar[i]} ", end = "")
    print("\n")
    obtener_color("Defecto")
    print("Perdiste!")

def cargar_jugador(nombre, clave):
    '''
    Función: cargar_jugador
    Descripción:
        Carga al archivo.csv el nombre y clave que recibe por parametro.
    Parametro:
        nombre: String que recibe como parametro.
        clave: String que recibe como parametro.
    '''
    registro=open('usuarios.csv','a')
    registro.write(nombre+','+clave+'\n')
    registro.close()
       
def ingreso_jugadores(jugador, jugadores_y_puntos):
    '''
    Función: ingreso_jugadores
    Parámetros:
        jugador: variable tipo string
        jugadores_y_puntos: diccionario
    Descripción: 
        Crea un diccionario con los nombres como claves y de valor sus puntajes.  
    Salidas:
        Nos retorna el diccionario.
    '''
    if jugador not in jugadores_y_puntos.keys():
        jugadores_y_puntos[jugador] = 0 
    
    return jugadores_y_puntos

def obtener_color(color):
    colores = {
        'Verde': '\x1b[32m',
        'Amarillo': '\x1b[33m',
        'GrisOscuro': '\x1b[90m',
        'Defecto': '\x1b[39m'
    }
    return colores[color]
