def obtener_color(color):
    colores = {
        "Verde": "\x1b[32m",
        "Amarillo": "\x1b[33m",
        "GrisOscuro": "\x1b[90m",
        "Defecto": "\x1b[39m"
    }
    return colores[color]

def fiuble():
    pal_adiv="MARES"
    print("Palabra a adivinar: ? ? ? ? ?")
    intento=input("Arriesgo:")
    intento=intento.upper()
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
                
        elif intento[pos] not in pal_adiv:
            color_3=obtener_color("GrisOscuro")
            colores.append(color_3)
        
        elif intento[pos] in pal_adiv and intento[pos] != pal_adiv[pos]:
            color_2=obtener_color("Amarillo")
            colores.append(color_2)
            
        elif intento[pos] == pal_adiv[pos]:
            color_1 = obtener_color("Verde") 
            colores.append(color_1)
                
    print(f"\nPalabra a adivinar: {pal_adiv[0]} {pal_adiv[1]} {pal_adiv[2]} {pal_adiv[3]} {pal_adiv[4]}")
    print("Arriesgo:",colores[0] + intento[0],colores[1] + intento[1], colores[2] + intento[2], colores[3] + intento[3], colores[4] + intento[4], obtener_color ("Defecto"))
    
    if pal_adiv==intento:
        print('Ganaste!')
    else:
        print('Perdiste!')
fiuble()
