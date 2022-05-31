import time

def cronometro(comienzo, final):
    '''
    Función: cronometro
    Parámetros:
        comienzo: inicia contador.
        final: detiene contador.
    Salidas:
        Devuelve los minutos y segundos tardados en finalizar el juego.
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