from typing import Any

import validacion


coleccion = {
    "1": {"descripcion":"descripcion1", "funcion":"funcion1"},
    "2": {"descripcion":"descripcion2", "funcion":"funcion2"},
    }


titulin="soy un titulo"
def mostrar(titulo:str, opciones:dict[str, dict[str, Any]]):
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



