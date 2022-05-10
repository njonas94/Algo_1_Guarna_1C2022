def es_primo(numero):
    if numero >= 2:
        for n in range(2, int(numero**0.5) + 1):
            if numero%n == 0:
                return False
        return True

def filtrar_primos(numeros, menor_numero):
    numeros_filtrados = []
    for numero in numeros:
        if es_primo(numero) and numero > menor_numero:
            numeros_filtrados.append(numero)

    return numeros_filtrados


def ordenar_por_longitud_de_tuplas(tuplas):
    tuplas_ordenadas = []
    for i in range(len(tuplas)):
        if i == 0:
            tuplas_ordenadas.append(tuplas[i])
        elif len(tuplas[i]) <= len(tuplas_ordenadas[0]):
            tuplas_ordenadas.insert(0 ,tuplas[i])
        elif len(tuplas[i]) >= len(tuplas_ordenadas[-1]):
            tuplas_ordenadas.append(tuplas[i])

    tuplas_ordenadas.reverse()

    return tuplas_ordenadas

