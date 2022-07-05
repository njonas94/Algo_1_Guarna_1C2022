from datetime import datetime
import time

def cronometro(comienzo, final):
    '''
    Función: cronometro
    Descripción: 
        Evalua y da formato al tiempo tardado en la ronda.
    Parámetros:
        Comienzo: tiempo en el que comienza el juego.
        Final: tiempo en el que termina el juego.
    Salidas:
        Devuelve una lista con los minutos y segundos tardados en finalizar el juego.
    '''
    tiempo_tardado=(final-comienzo)
    if tiempo_tardado>=60:
        minutos=tiempo_tardado//60
        segundos=round(tiempo_tardado%60,0)
        tiempo=[minutos, segundos]
    else:
        minutos=0
        segundos=round(tiempo_tardado,0)
        tiempo=[minutos, segundos]
    
    return tiempo

def fecha_y_hora():
    dia=datetime.today().strftime('%Y-%m-%d')
    hora=datetime.today().strftime('%H:%M')
    
    return [dia,hora]

def cambiar_tilde(intento_sin_validar):
    '''
    Función: cambiar_tilde
    Parámetro:
        intento_sin_validar: cadena de caracteres ingresado por el usuario.
    Salidas:
        Devuelve la palabra sin acentos.
    '''
    a = 'áéíóúýäëïöüÿàèìòùâêîôûú'
    b = 'aeiouyaeiouyaeiouaeiouu'
    palabra_sin_acento = intento_sin_validar.maketrans(a, b)
    intento_sin_validar_sin_tilde = intento_sin_validar.translate(palabra_sin_acento)

    return intento_sin_validar_sin_tilde

