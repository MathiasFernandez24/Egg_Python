array = []
while True:
    num_ingresado = input("Ingrese un numero: ")
    print(type(num_ingresado))
    if (num_ingresado == ""):
        print("------FIN PROGRAMA------")
        break
    array.append((int(num_ingresado),))

array_plano = [array[i][0]for i in range(len(array))]

print("array con tuplas -> ", array)
print("array desempaquetado ->", array_plano)
