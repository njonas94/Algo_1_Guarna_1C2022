import random
from utiles import *

palabra_ingresada = ""
lista_palabra_a_adivinar = ["?", "?", "?", "?", "?"]

def generar_palabra_a_adivinar():
    palabras_validas = obtener_palabras_validas()
    
    return random.choice(palabras_validas)

palabra_a_adivinar = generar_palabra_a_adivinar()

def acumular_intentos(palabra_ingresada, intentos_ingresados):
    if palabra_ingresada not in intentos_ingresados:
        intentos_ingresados.append(palabra_ingresada)
    
    return

def mostrar_juego(lista_palabra_ingresada):
    print("Palabra a adivinar: ", end="")
    for letra in lista_palabra_ingresada:
        print(letra + " ", end= "")

    return

def main():
    palabra_a_adivinar = generar_palabra_a_adivinar()
    intentos_ingresados = [["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?"]]
    while True:
        mostrar_juego()
        break

    return

def procesar_intento(pal_adiv, intento):
    colores=[]
    for pos in range(len(pal_adiv)):
        if (pal_adiv.count(intento[pos])==1 and intento.count(intento[pos])==2):
            pos_1=intento.index(intento[pos])
            pos_2=intento.rindex(intento[pos])
            
            if ((pos==pos_1 and pos_1==pal_adiv.index(intento[pos_1])) or (pos==pos_2 and pos_2==pal_adiv.index(intento[pos_2]))):
                color_1 = obtener_color("Verde") 
                colores.append(color_1)
                                
            elif ((pos==pos_2 and pos_1==pal_adiv.index(intento[pos_1])) or (pos==pos_1 and pos_2==pal_adiv.index(intento[pos_2]))):
                color_3 = obtener_color("GrisOscuro") 
                colores.append(color_3)
                               
            elif (pos==pos_1 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                color_2=obtener_color("Amarillo") 
                colores.append(color_2)
                              
            elif (pos==pos_2 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                color_3 = obtener_color("GrisOscuro") 
                colores.append(color_3)
                
        elif intento[pos] == pal_adiv[pos]:
            color_1 = obtener_color("Verde") 
            colores.append(color_1)
       
        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            color_2=obtener_color("Amarillo")
            colores.append(color_2)
            
        elif intento[pos] not in pal_adiv:
            color_3=obtener_color("GrisOscuro")
            colores.append(color_3)

    return colores

#print("Arriesgo:",colores[0] + intento[0].upper(),colores[1] + intento[1].upper(), colores[2] + intento[2].upper(), colores[3] + intento[3].upper(), colores[4] + intento[4].upper(), obtener_color ("Defecto"))


mostrar_juego(lista_palabra_a_adivinar)
"""
Pruebas

print(intentos_ingresados)
print(intentos_ingresados[0])
print(intentos_ingresados[1])
print("prueba")

"""