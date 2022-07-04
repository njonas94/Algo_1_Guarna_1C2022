from utiles import *


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

#____________________________Funciones etapa 7 relacionadas con INTERFAZ GRAFICA________________________#
       
def leer_archivo(archivo, default):#FUNCION 2
    linea=archivo.readline()
    if linea:
        lista=linea.rstrip('\n').split(',')
    else:
        lista=default.split(',')    
    return lista

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

def cargar_jugador(nombre, clave):
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
