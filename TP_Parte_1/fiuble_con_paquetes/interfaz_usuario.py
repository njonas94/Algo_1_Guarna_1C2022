from utiles import *

def mostrar_palabra(palabra_ingresada):
    '''
    Muestra por pantalla las palabras en el formato deseado.
    '''
    for letra in palabra_ingresada:
        print(letra + " " + obtener_color("Defecto"), end = "")
    print()

'''LA FUNCION DE JUEGO_TERMINADO SE PODRÍA BORRAR, NO ES LLAMADA POR NINGUNA FUNCION.
   SU ESTRUCTURA SE ENCUENTRA REPETIDA EN JUGABILIDAD LINEA 97 A 100, Y EN FIUBLE LINEA 23 A 26'''
#def juego_terminado(lista_de_intentos_ingresados, palabra_adivinar):
#    '''
#    Muestra en terminal la "Palabra a adivinar" y los intentos.
#    '''
#    print("Palabra a adivinar: ", end = "")
#    mostrar_palabra(pal_adiv)
#    for intento in lista_de_intentos_ingresados:
#        mostrar_palabra(intento)

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
