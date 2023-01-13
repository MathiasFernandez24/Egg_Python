def funcion(lista: list, var1):
    if (var1 in lista):
        print("--> Ingresa al error")
        raise ValueError(
            f"Error: No puedes agregar el elemento '{var1}' porque ya existe en la lista.")
    print("-->EXITO")
    print(lista, var1)


funcion([1, 2, 3], "1")
funcion([1, 2, 3], 1)
