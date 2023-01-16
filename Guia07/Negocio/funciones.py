def crear_articulo():
    while True:
        nombre = input("Ingrese Nombre: ")
        if len(nombre)>=3 and len(nombre)<=100 and nombre.isdigit() == False:
            break

    while True:
        try:
            precio = float(input("Ingrese Precio: "))
            if precio>0:
                break
        except Exception as e:
            print("     --debe ser un numero--")

    while True:
        try:
            cantidad = int(input("Ingrese Cantidad: "))
            if cantidad > 0 and cantidad<1000000:
                break
        except Exception as e:
            print("     --debe ser un numero--")
    valor={
        "nombre": nombre,
        "precio":precio,
        "cantidad":
    }

    
crear_articulo()
# print("asd123".isdigit())