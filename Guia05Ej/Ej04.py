numeros_validos = [1, 3, 6, 9]
while True:
    # bandera = True
    # numero = int(input("ingrese un numero: "))
    # for i in numeros_validos:
    #     if (numero == i):
    #         print("APROBADO")
    #         bandera = False
    # if bandera:
    #     print("DENEGADO")

    numero = int(input("ingrese un numero: "))
    if numero in numeros_validos:
        print("APROBADO")
    else:
        print("DENEGADO")
