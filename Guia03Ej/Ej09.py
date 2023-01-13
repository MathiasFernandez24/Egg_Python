num_01 = int(input("Numero 1: "))
num_02 = int(input("Numero 2: "))

while True:
    eleccion = input("""
    a) - sumar
    b) - restar
    c) - multiplicar
    d) - cerrar programa
    """).lower()

    if eleccion == "a":
        print(num_01+num_02)
    elif eleccion == "b":
        print(num_01-num_02)
    elif eleccion == "c":
        print(num_01*num_02)
    elif eleccion == "d":
        print("Programa finalizado, vuelta prontos")
        break
    else:
        print("opcion no disponible")
