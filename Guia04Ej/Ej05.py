letras = []
while True:
    letra = input("Ingrese una letra: ")
    if (letra == ""):
        print("PROGRAMA FINALIZADO")
        break
    letras.insert(0, letra[::-1])

    print("letras -> ", letras)
