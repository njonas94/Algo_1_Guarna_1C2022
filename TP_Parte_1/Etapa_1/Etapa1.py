def obtener_color(color):
    colores = {
        "Verde": "\x1b[32m",
        "Amarillo": "\x1b[33m",
        "GrisOscuro": "\x1b[90m",
        "Defecto": "\x1b[39m"
    }
    return colores[color]

def obtener_palabras_validas():
    return ["abran", "abria", "acojo", "actuo", "aguda", "agudo", "algas", \
            "almas", "alojo", "alojo", "altas", "altos", "andes", "anima", \
            "apodo", "arcos", "ardan", "ardes", "arios", "azote", "bajas", \
            "bajan", "bardo", "bates", "bayas", "bebes", "besen", "besos", \
            "botas", "bodas", "bondi", "bonos", "borre", "botan", "botes", \
            "bruta", "cagas", "cajas", "callo", "calma", "campo", "canas", \
            "capas", "caros", "casan", "casas", "cazan", "cazas", "caida", \
            "caido", "ceder", "cenas", "cepas", "ceras", "cerdo", "cerco", \
            "ceros", "cerro", "ciega", "ciego", "cines", "clava", "clavo", \
            "calvo", "cogen", "coger", "colas", "coles", "coman", "conos", \
            "capas", "capaz", "copos", "copas", "coral", "corra", "corre", \
            "cosas", "coses", "croar", "cruje", "cuida", "culta", "culto", \
            "cunas", "curso", "dagas", "datos", "debes", "dedos", "densa", \
            "dijes", "doman", "domar", "donan", "donas", "dones", "dotes", \
            "dudan", "dunas", "duros", "echas", "echan", "edita", "ellos", \
            "emana", "emoji", "enoja", "enojo", "entes", "envio", "erizo", \
            "errar", "error", "espia", "euros", "evita", "evito", "falla", \
            "falta", "fetos", "filas", "firme", "focos", "fosos", "frias", \
            "fugas", "fumar", "gafas", "galas", "galos", "ganas", "gases", \
            "gatos", "genes", "giras", "giros", "goles", "gorra", "grave", \
            "grite", "grito", "hielo", "heces", "habia", "hacen", "hacia", \
            "hacha", "hecho", "hijas", "hilos", "hojas", "hugos", "ideas", \
            "iglus", "islas", "india", "jefes", "jerga", "jodas", "jugos", \
            "jamon", "kenia", "kodak", "kayak", "lacra", "libro", "lados", \
            "lagos", "lamen", "larga", "latas", "lazos", "lejos", "lenta", \
            "lento", "libre", "linda", "locas", "locos", "lomos", "loros", \
            "losas", "luces", "leche", "lucha", "luche", "magos", "malas", \
            "males", "malos", "mamas", "manca", "manco", "manos", "manda", \
            "mapas", "marco", "mares", "matar", "mayas", "mazos", "mesas", \
            "metas", "metes", "miles", "minas", "mirar", "mitos", "modas", \
            "mojar", "modos", "mojan", "moles", "monas", "monos", "monte", \
            "moras", "moros", "mozas", "mocos", "mulas", "multa", "muros", \
            "musas", "nabos", "nadar", "naves", "nazis", "nubes", "nudos", \
            "nieve", "nunca", "nacer", "necio", "necia", "obras", "odiar", \
            "odios", "ollas", "ombus", "ondas", "onzas", "opera", "orcas", \
            "orden", "otras", "ovulo", "paces", "pajas", "palas", "palma", \
            "palos", "panes", "parda", "parar", "pares", "pases", "patos", \
            "pecas", "peces", "penas", "pense", "perdi", "pesas", "pesca", \
            "pesos", "pesas", "peces", "pican", "pedir", "pisar", "pleno", \
            "plena", "pocas", "pocos", "podar", "poder", "podia", "ponen", \
            "poner", "posee", "pozos", "pùjar", "pujan", "pulen", "pulir", \
            "pumas", "puros", "quema", "quise", "quito", "queso", "rabia", \
            "rabos", "ramos", "ratas", "ratos", "redes", "rejas", "remos", \
            "retos", "reyes", "rifas", "rimas", "riman", "rimar", "roban", \
            "rodan", "rojas", "rojos", "rosas", "rotar", "rugir", "runas", \
            "rusas", "rusos", "sabia", "serio", "sacar", "salgo", "salga", \
            "salta", "salto", "selva", "sanar", "sapos", "sedes", "santa", \
            "seria", "serio", "sobar", "sonar", "subir", "suela", "sumar", \
            "super", "tacos", "talar", "tejas", "temas", "temen", "temer", \
            "tener", "tenso", "tensa", "tiros", "titan", "togas", "tomar", \
            "tonta", "tonto", "torpe", "traje", "trios", "urnas", "untar", \
            "umami", "urgar", "vacas", "vagos", "vagas", "vasca", "velos", \
            "venas", "vidas", "vigas", "vinos", "volar", "votos", "votar", \
            "video", "yates", "yemas", "yenes", "yogur", "zetas", "zonas", \
            "zurda", "zurdo", "zorro"]
def fiuble():
    pal_adiv="mares"
    print("Palabra a adivinar: ? ? ? ? ?")
    intento=input("Arriesgo:")
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
                
    print(f"\nPalabra a adivinar: {pal_adiv[0].upper()} {pal_adiv[1].upper()} {pal_adiv[2].upper()} {pal_adiv[3].upper()} {pal_adiv[4].upper()}")
    print("Arriesgo:",colores[0] + intento[0].upper(),colores[1] + intento[1].upper(), colores[2] + intento[2].upper(), colores[3] + intento[3].upper(), colores[4] + intento[4].upper(), obtener_color ("Defecto"))
    
    if pal_adiv==intento:
        print('Ganaste!')
    else:
        print('Perdiste!')
fiuble()
