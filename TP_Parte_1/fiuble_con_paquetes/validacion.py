from utiles import *
from procesar_archivos import *

def no_es_alfabetico (intento_sin_validar):
    return not intento_sin_validar.isalpha()

def longitud_palabra (intento_sin_validar, LONGITUD_PALABRAS):
    return len(intento_sin_validar)!= LONGITUD_PALABRAS

def validar_palabra (intento_sin_validar, diccionario_palabras_validas):
    return not no_es_alfabetico (intento_sin_validar) and intento_sin_validar not in diccionario_palabras_validas

def validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):
    return intento_sin_validar.upper() in lista_de_intentos_ingresados

def longitud_y_alfabetica(intento_sin_validar, LONGITUD_PALABRAS):
    return not intento_sin_validar.isalpha() and len(intento_sin_validar) != LONGITUD_PALABRAS

def validacion_intento_ingresado(intento_sin_validar, lista_de_intentos_ingresados, diccionario_palabras_validas, LONGITUD_PALABRAS):
    '''
    Función: validacion_intento_ingresado
    Parámetro:
        intento_sin_validar: cadena de caracteres ingresado por el usuario.
        lista_de_intentos_ingresados: lista de cadenas de caracteres.
    Salidas:
        Devuelve la palabra en mayúscula.
    '''
    intento_sin_validar = cambiar_tilde(intento_sin_validar.lower())
    while no_es_alfabetico (intento_sin_validar) or validar_palabra (intento_sin_validar, diccionario_palabras_validas) or validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):

        if longitud_y_alfabetica(intento_sin_validar, LONGITUD_PALABRAS):
            print(f"Palabra inválida, tiene que ser de {LONGITUD_PALABRAS} letras y no puede contener número/s ni caracteres especiales.")

        elif no_es_alfabetico (intento_sin_validar):
            print("La palabra no tiene que contener número/s ni caracteres especiales.")

        elif longitud_palabra (intento_sin_validar, LONGITUD_PALABRAS): 
            print(f"La palabra tiene que ser de {LONGITUD_PALABRAS} letras.")

        elif validar_intento_duplicado (intento_sin_validar, lista_de_intentos_ingresados):
            print("La palabra ya habia sido ingresada.")

        elif validar_palabra (intento_sin_validar, diccionario_palabras_validas):
            print("La palabra no se encuentra en la lista de palabras válidas.")

        intento_sin_validar = input(f"Ingrese una palabra valida de {LONGITUD_PALABRAS} letras: ")
        intento_sin_validar = cambiar_tilde(intento_sin_validar.lower())

    return intento_sin_validar.upper()

def validar_registro(usuario,clave,confirmacion_clave):
    '''
    Funcion: validar_registro
    Parámetros:
        usuario: variable de tipo string, nombre del jugador
        clave: variable de tipo string, contraseña
        confirmacion_clave: variable de tipo string, contraseña repetida
    Descripcion:
        Corrobora si el usuario y clave son validos para registrarse
    Salida:
        Lista con el estado del usuario y la clave
    '''
    registro=open('usuarios.csv','r')
    jugador,contrasenia=leer_archivo(registro,',')
    password=validar_clave(clave,confirmacion_clave)
    nombre='invalido'
    while jugador!='' and usuario!=jugador:
        jugador,contrasenia=leer_archivo(registro,',')
    if jugador=='' and usuario!=jugador:
        nombre=validar_usuario(usuario) 
    elif jugador!='' and usuario==jugador:
        nombre='ocupado'
    registro.close()

    return [nombre,password]
 
def validar_usuario(usuario):
    '''
    Funcion: validar_usuario
    Parámetros:
        usuario: variable de tipo string, nombre del jugador
    Descripcion:
        Corrobora si el usuario es valido para registrarse
    Salida:
        Devuelve la el estado del usuario, valida o invalida
    '''
    condiciones_cumplidas=0
    cantidad_letras=0
    cantidad_numeros=0
    cantidad_guion_bajo=0
    cantidad_especiales=0
    posicion=0
    if 4<=len(usuario)<=15 and "_" in usuario:
        condiciones_cumplidas+=2
        while posicion<len(usuario) and (2<=condiciones_cumplidas<=4 and cantidad_especiales==0):        
            if usuario[posicion].isalpha() and cantidad_letras==0:
                condiciones_cumplidas+=1
                cantidad_letras+=1
                
            elif usuario[posicion].isnumeric() and cantidad_numeros==0:
                condiciones_cumplidas+=1
                cantidad_numeros+=1
                            
            elif not usuario[posicion].isalnum() and usuario[posicion]!='_' and cantidad_especiales==0 :
                cantidad_especiales+=1
            posicion+=1
   
    if condiciones_cumplidas==4 and cantidad_especiales==0:
        estado='valido'
    else:
        estado='invalido'

    return estado
            
def validar_clave(clave,confirmacion_clave):
    '''
    Funcion: validar_clave
    Parámetros:
        clave: variable de tipo string, contraseña
        confirmacion_clave: variable de tipo string, contraseña repetida
    Descripcion:
        Verifica si la clave ingresada es valida y si su copia es igual.
    Salida:
        Devuelve la el estado de la clave, valida o invalida
    '''
    condiciones_cumplidas=0
    cantidad_mayusculas=0
    cantidad_minusculas=0
    cantidad_numeros=0
    cantidad_guion=0
    cantidad_especiales=0
    posicion=0
    if 8<=len(clave)<=12:
        condiciones_cumplidas+=1
        while posicion<len(clave) and (1<=condiciones_cumplidas<=5 and cantidad_especiales==0):        
            if clave[posicion].isupper() and cantidad_mayusculas==0:
                condiciones_cumplidas+=1
                cantidad_mayusculas+=1
                
            elif clave[posicion].islower() and cantidad_minusculas==0:
                condiciones_cumplidas+=1
                cantidad_minusculas+=1
                
            elif clave[posicion].isnumeric() and cantidad_numeros==0:
                condiciones_cumplidas+=1
                cantidad_numeros+=1
                
            elif clave[posicion] in ('_','-') and cantidad_guion==0:
                condiciones_cumplidas+=1
                cantidad_guion+=1
            
            elif not clave[posicion].isalnum() and clave[posicion]not in ('_','-','á','é','í','ó','ú') and cantidad_especiales==0 :
                cantidad_especiales+=1
            posicion+=1
        
    if condiciones_cumplidas==5 and cantidad_especiales==0 and clave==confirmacion_clave:
        estado='valido'
    else:
        estado='invalido'
            
    return estado

def validar_ingreso(usuario,clave):
    '''
    Función: validar_ingreso
    Parámetros:
        usuario: cadena de caracteres, proviene del ingreso en la interfaz grafica.
        clave:cadena de caracteres, proviene del ingreso en la interfaz grafica
    Descripción: 
        Corrobora si los datos ingresados por el usuario estan cargados en el archivo de usuarios  
    Salidas:
        variable de tipo string
    '''
    registro=open('usuarios.csv','r')
    jugador,contrasenia=leer_archivo(registro,',')
    while jugador!='' and (jugador!=usuario or contrasenia!=clave) and not(jugador==usuario and contrasenia==clave):
        jugador,contrasenia=leer_archivo(registro, ',')
        
    if jugador!='' and (jugador==usuario and contrasenia==clave):
        condicion='permitido'
        
    elif jugador=='':   
        condicion=''
        
    registro.close()
    
    return condicion