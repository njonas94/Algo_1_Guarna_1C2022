import re


def leer_archivos(archivo):
    for linea in archivo:
        if linea:
            linea = re.sub(r'[^\w\s]', '', linea)
            linea = linea.rstrip("\n").split()
            for palabra in linea:
                if not palabra.isalpha():
                    linea.remove(palabra)
