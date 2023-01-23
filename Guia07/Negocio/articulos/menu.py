import pprint
from .funcionalidades import crear_articulo, mostrar_articulos
import usuario

titulo_02="Menu Articulos"
coleccion_02 = {
    "1": {"descripcion":"Ver Articulos", "funcion":"funcion1"},
    "2": {"descripcion":"Agregar un articulo", "funcion":"funcion2"},
    "3": {"descripcion":"Modificar un artículo", "funcion":"funcion2"},
    "4": {"descripcion":"Eliminar un artículo", "funcion":"funcion2"},
    "x": {"descripcion":"Salir", "funcion":"funcion2"},
}

def menu_articulos(carrito):
    while True:
            usuario.mostrar(titulo_02,coleccion_02)
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

