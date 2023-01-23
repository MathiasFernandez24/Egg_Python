from typing import Any
import articulos

import validacion

titulo_01="Menu Usuario"
coleccion_01 = {
    "1": {"descripcion":"Articulos", "funcion":"funcion1"},
    "2": {"descripcion":"Clientes", "funcion":"funcion2"},
    "3": {"descripcion":"Ventas", "funcion":"funcion2"},
    "x": {"descripcion":"Salir", "funcion":"funcion2"},
}

def mostrar(titulo:str, opciones:dict[str, dict[str, Any]]):
    """Recibe un titulo (string) y un diccionario ene l siguiente formato-> opciones(editable):{descripcion(fijo):descripcion1(editable), funcion(fijo):funcion1(editable)}, lo muestra con estilos"""
    print(f"---------{titulo}---------")
    for a,b in opciones.items():
        c= b["descripcion"]
        d= b["funcion"]
        print(f"{a} - {c}")

def leer_opcion()->None|str:
    while True:
        msj = input("Ingrese una opcion: ")
        texto= validacion.validar.cadena_vacía(msj)
        print(texto)

def menu_usuario(carrito):
    while True:
        mostrar(titulo_01,coleccion_01)
        opcion= input("seleccione una opcion: ")
        if opcion=="1":
            articulos.menu_articulos(carrito)
        elif opcion=="2":
            print("menu2")
        elif opcion=="3":
            print("menu3")
        elif opcion=="x":
            break

