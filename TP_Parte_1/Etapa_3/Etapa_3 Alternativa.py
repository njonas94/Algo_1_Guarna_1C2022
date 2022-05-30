from utiles import *
import random
'''
    Función: generar_palabra_a_adivinar
    Salidas:
        Devuelve una palabra en mayúscula, seleccionada aleatoriamente de la lista de palabras válidas.
'''
def generar_palabra_a_adivinar():
    palabras_validas = obtener_palabras_validas()
    palabra=random.choice(palabras_validas)
    return palabra.upper()

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
        Devuelve la palabra sin caracteres con acentos.
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
        pal_adiv: palabra a adivinar, cadena de caracteres.
        intento: palabra ingresada por el usuario, cadena de caracteres.
    Salidas:
        Devuelve una lista con las palabra ingresada.
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
                        #print(adivinar)
                                    
                elif ((pos==pos_2 and pos_1==pal_adiv.index(intento[pos_1])) or (pos==pos_1 and pos_2==pal_adiv.index(intento[pos_2]))):
                    color_3 = obtener_color("GrisOscuro") 
                    palabras[orden_ingreso][pos]=(color_3+intento[pos])
                    #print(adivinar)
                                   
                elif (pos==pos_1 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                    color_2=obtener_color("Amarillo") 
                    palabras[orden_ingreso][pos]=(color_2+intento[pos])
                    #print(adivinar)
                    
                elif (pos==pos_2 and pos_1!=pal_adiv.index(intento[pos_1]) and pos_2!=pal_adiv.index(intento[pos_1])):
                    color_3 = obtener_color("GrisOscuro") 
                    palabras[orden_ingreso][pos]=(color_3+intento[pos])
                    #print(adivinar)
                    
            elif intento[pos] not in pal_adiv:
                color_3=obtener_color("GrisOscuro")
                palabras[orden_ingreso][pos]=(color_3+intento[pos])
                #print(adivinar)
                
            elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
                color_2=obtener_color("Amarillo")
                palabras[orden_ingreso][pos]=(color_2+intento[pos])
                #print(adivinar)
                
            elif intento[pos] == pal_adiv[pos]:
                color_1 = obtener_color("Verde") 
                palabras[orden_ingreso][pos]=(color_1+intento[pos])
                if pal_adiv[pos] != adivinar[pos]:
                    adivinar[pos]=pal_adiv[pos]
                    #print(adivinar)
                    
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

def fiuble():
    pal_adiv=generar_palabra_a_adivinar()
    print("Palabra a adivinar: ? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?\n? ? ? ? ?")
    intento=input("Arriesgo:")
    intento=validacion(intento)
    lista_de_intentos_ingresados=desarrollo_intentos(pal_adiv, intento)
    if pal_adiv in lista_de_intentos_ingresados:
        print('Ganaste!')
    else:
        print('Perdiste!')
        print(f'La palabra era: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]} {obtener_color("Defecto")}')
fiuble()