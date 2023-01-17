from funciones import crear_articulo    
import pprint

carrito={}

while True:
    print("""
------------
1. Artículos
2. Clientes
3. Ventas
x. Salir
""")
    opcion= input("seleccione una opcion: ")
    if opcion=="1":
        while True:

            print("""
        ARTÍCULOS
        1. Ver artículos
	2. Agregar un artículo
	3. Modificar un artículo
	4. Eliminar un artículo
	x. Salir""")
            opcion= input("seleccione una opcion: ")
            if opcion == "1":
                print("     ----INVENTARIO----")
                pprint.pprint(carrito)
            elif opcion == "2":
                [codigo, valores] = crear_articulo(carrito)
                carrito.update({codigo:valores})
            elif opcion == "3":
                print("sub-menu3")
            elif opcion == "4":
                print("sub-menu4")
            elif opcion == "x":
                break


    elif opcion=="2":
        print("menu2")
    elif opcion=="3":
        print("menu3")
    elif opcion=="x":
        break