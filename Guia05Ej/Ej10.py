from pprint import pprint

gondola = {"artículo": {}}

while True:
    pregunta_agregar_gondola = input(
        "Agregar productos a la gondola? (s/n): ").lower()
    if pregunta_agregar_gondola == "s":
        print("AGREAGR ARTICULO A GONDOLA:")
# Validador de Codigo
        while True:
            codigo = int(input("Numero de Codigo: "))
            if (codigo not in gondola["artículo"]):
                break
            else:
                print("El codigo del articulo ya existe")
# Validador de Nombre
        while True:
            nombre = input("Nombre articulo: ")
            if nombre != "":
                break
            else:
                print("No puede estar vacio el nombre")
# Validador de Precio
        while True:
            precio = float(input("Precio Articulo: "))
            if precio >= 0:
                break
            else:
                print("El precio no puede ser cero o menor")
# Validador de Stock
        while True:
            stock = int(input("Stock inicial Articulo: "))
            if stock >= 0:
                break
            else:
                print("El stock no puede ser cero o menor")

        gondola["artículo"][codigo] = {
            "nombre": nombre, "precio": precio, "stock": stock}

        pprint(gondola)
    else:
        break

print("---BIENVENIDOS AL CARRITO---")
carrito = {"articulos": [], "total": 0}
while True:
    pregunta_agregar_carrito = input(
        "Agregar productos al carrito? (s/n): ").lower()
    if pregunta_agregar_carrito == "s":
        print("AGREAGR ARTICULO AL CARRITO:")
        codigo = int(input("Codigo del producto a agregar: "))
        if (codigo in gondola["artículo"]):
            nombre = gondola["artículo"][codigo]["nombre"]
            precio = gondola["artículo"][codigo]["precio"]
            stock = gondola["artículo"][codigo]["stock"]
            while True:
                cantidad_agregar_a_carrito = int(
                    input(f"Cantidad articulos para agregar al carrito(max: {stock}): "))
                if cantidad_agregar_a_carrito <= stock:
                    break
                else:
                    print("No hay esa cantidad disponible")
            articulo_carrito = {
                "nombre": nombre, "precio": precio, "cantidad": cantidad_agregar_a_carrito}
            carrito["articulos"].append(articulo_carrito)
            carrito["total"] += cantidad_agregar_a_carrito*precio
            gondola["artículo"][codigo]["stock"] -= cantidad_agregar_a_carrito
        else:
            print("El codigo del articulo no existe")
    else:
        break
    pprint(carrito)
    pprint(gondola)
