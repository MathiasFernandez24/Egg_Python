contador = 0
vueltas = int(input("Cantidad de vueltas: "))
largo = 0

while contador < vueltas:
    contador += 1
    texto = input("Ingrese texto: ")
    largo += len(texto)
else:
    print("Letras totales ingresadas", largo)
