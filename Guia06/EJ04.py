def promedio(*args):
    """calcula el promedio de los numeros ingresados como parametros"""
    suma = sum(args)
    print(f"suma -> {suma}")
    promedio = suma / len(args)
    return promedio


cantidad_de_numeros = int(input("Cantidad de numeros a ingresar: "))
coleccion = set()
for item in range(cantidad_de_numeros):
    x = int(input("Agregar numero: "))
    coleccion.add(x)

print(coleccion)

a = promedio(*coleccion)
print(f"El promedio de {coleccion} es {a}")
