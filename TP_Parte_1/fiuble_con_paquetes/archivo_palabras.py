def archivo_palabras(lista_ordenada):
    archivo = open("palabras.csv","w")
    for palabra in lista_ordenada:
        archivo.write(palabra[0] + "," + str(palabra[1]) + "," + str(palabra[2]) + "," + str(palabra[3]) + "\n")
    archivo.close()