def validacion (palabra_ingresada):
    hola=True
    if palabra_ingresada.isalpha()!=True:
        hola=False
        print("La palabra no puede contener numeros ni caracteres especiales, porfavor ingrese de nuevo la palabra")
    if len(palabra_ingresada) != 5:
        hola=False
        print("La palabra solo puede contener 5 letras")

    if hola:
        palabra_ingresada_mayus = palabra_ingresada.upper()
        a = 'ÁÉÍÓÚÝÄËÏÖÜŸ'
        b = 'AEIOUYAEIOUY'
        palabra_sin_acento=palabra_ingresada_mayus.maketrans(a,b)
        arriesgo=palabra_ingresada_mayus.translate(palabra_sin_acento)
              
    return arriesgo
#posibles arriesgos  arriesgo="SóFÁSs1"  arriesgo="SóFÁSS"   arriesgo="SóFÁ1" 
arriesgo="SóFÁS"
print("arriesgo",validacion(arriesgo))

