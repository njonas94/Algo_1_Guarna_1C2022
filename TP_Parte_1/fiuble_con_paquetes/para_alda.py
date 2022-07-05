def crear_diccionario_usuarios_datos(turnos):
    '''
    Función: crear_diccionario_usuarios_datos
    Descripción:
        Crea el diccionario con los usuarios correspondientes como clave y 3er valor.
    Parametros:
        turnos: Lista de turnos.
    Salida:
        Retorna diccionario creado con los nombres de usuarios cargados.
    '''
    usuarios_datos = {}
    usuarios_datos[turnos[0]] = ['','','',0,0]
    usuarios_datos[turnos[0]][-3] = turnos[0]
    usuarios_datos[turnos[1]] = ['','','',0,0]
    usuarios_datos[turnos[1]][-3] = turnos[1]
    return usuarios_datos

def cargar_hora(turnos,fecha,hora,usuarios_datos):
    '''
    Función: cargar_hora
    Descripción:
        Cargar la fecha/hora en el diccionario que recibe como parametro.
    Parametros:
        turnos: Lista de turnos.
        fecha:  String con la fecha.
        hora: String con la hora.
        usuarios_datos: Diccionario con los usuarios.
    Salida:
        Retorna diccionario con los datos fecha/hora cargados.
    '''
    lista_jugadores=[turnos[0],turnos[1]]
    for jugador in lista_jugadores:
        usuarios_datos[jugador][0]=fecha
        usuarios_datos[jugador][1]=hora
    return usuarios_datos


def cargar_aciertos_e_intentos(lista_de_intentos_ingresados, palabra_adivinar, usuarios_datos, turnos):
    '''
    Función: cargar_aciertos_e_intentos
    Descripción:
        Agrega los intentos/aciertos correspondientes al diccionario usuarios_datos.
    Parametros:
        lista_de_intentos_ingresados: Lista de intentos ingresados.
        palabra_adivinar: String palabra a adivinar.
        usuarios_datos: Diccionario con los usuarios.
        turnos: Lista de turnos.
    Salida:
        Retora lista de listas con los valores de los usuarios en el diccionario que recibe como parametro.    
    '''    
    if palabra_adivinar not in lista_de_intentos_ingresados and len(lista_de_intentos_ingresados)==5:
        usuarios_datos[turnos[0]][-1]+=3
        usuarios_datos[turnos[1]][-1]+=2

    elif palabra_adivinar in lista_de_intentos_ingresados:
        indice = len(lista_de_intentos_ingresados)-1
        
        jugador_acierto = turnos[indice]
        if indice ==0:
            jugador_fallo = turnos[indice-2]
        else:
            jugador_fallo = turnos[indice-1]
        
        if len(lista_de_intentos_ingresados)==1:
            usuarios_datos[jugador_acierto][-1]+=1
            usuarios_datos[jugador_acierto][-2]+=1
            
        elif len(lista_de_intentos_ingresados)==2:
            usuarios_datos[jugador_acierto][-1]+=1
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=1
            
        elif len(lista_de_intentos_ingresados)==3:
            usuarios_datos[jugador_acierto][-1]+= 2
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=1
            
        elif len(lista_de_intentos_ingresados)==4:
            usuarios_datos[jugador_acierto][-1]+=2
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=2
           
            
        elif len(lista_de_intentos_ingresados)==5:
            usuarios_datos[jugador_acierto][-1]+=3
            usuarios_datos[jugador_acierto][-2]+=1
            usuarios_datos[jugador_fallo][-1]+=2               
    return usuarios_datos.values()
    
    
def limpiar_archivo(REINICIAR_PARTIDAS_CSV):
    '''
    Función: limpiar_archivo
    Descripcion:
        Resetear el archivo partidas.csv al final del juego en caso que asi se indique.
    Parametro:
        REINICIAR_PARTIDAS_CSV: Variable booleana del archivo configuración.
    '''
    if REINICIAR_PARTIDAS_CSV:
        reinicio = open("partidas.csv","w")
        reinicio.close()
    return
