def promedio(*args):
    promedio = 0
    for numero in args:
        promedio += numero
    promedio = promedio / len(args)
    return promedio


coleccion = {2, 3, 4, 5, 6}
a = promedio(*coleccion)
print(f"El promedio de {coleccion} es {a}")
