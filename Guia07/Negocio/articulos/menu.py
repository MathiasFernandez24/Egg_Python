import pprint
from .funcionalidades import crear_articulo, mostrar_articulos

def menu(carrito):
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
                mostrar_articulos(carrito)
            elif opcion == "2":
                [codigo, valores] = crear_articulo(carrito)
                carrito.update({codigo:valores})
            elif opcion == "3":
                print("sub-menu3")
            elif opcion == "4":
                print("sub-menu4")
            elif opcion == "x":
                break

