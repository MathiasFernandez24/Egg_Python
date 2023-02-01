from dataclasses import dataclass, asdict
from datetime import datetime
import locale
import datetime as dt 
import json

locale.setlocale(locale.LC_ALL, "es_AR") 

@dataclass
class Cliente():
    dni: str
    apellidos: str
    nombres: str
    nacimiento: datetime

def cliente_crear()-> Cliente:
    print("----Datos Cliente----")
    dni = input("Ingrese dni: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    while True:
        try:
            fecha= input("Ingrese fecha nacimiento en formato DD/MM/YYYY: ")
            nacimiento = datetime.strptime(fecha,"%d/%m/%Y")
            if nacimiento< datetime.today():
                break
            else:
                print("--> no podes nacer en el futuro... aún...")
        except Exception as e:
            print("--> Ingresa la fecha bien, pillin...")
    c = Cliente(dni,apellido,nombre,nacimiento)
    return c

def cliente_guardar(c:Cliente):
    diccionario= asdict(c)
    f=diccionario["nacimiento"]
    f=f.strftime("%d/%m/%Y")
    diccionario["nacimiento"]=f
    # texto = f"Nombre: {diccionario['nombres']}, Apellido: {diccionario['apellidos']}, DNI: {diccionario['dni']}, Fecha de Nacimiento: {diccionario['nacimiento']}"
    # fecha_creacion= datetime.today()
    # fecha_creacion=fecha_creacion.strftime(" - Creado: %A %d/%B/%Y %H:%M:%S")
    # texto=texto+fecha_creacion

    # nuevo_json = json.dumps(diccionario)


    with open("cliente.json","w") as a:
        json.dump(diccionario, a)
        # json.dump(nuevo_json, a)


c_01 = cliente_crear()
cliente_guardar(c_01)
# print(open(,"r"))

















# import json
# from pprint import pprint


# texto = """
# 	{
# 	"nombre":{
# 	    "nombres":"Regina",
# 	    "apellidos":null
# 	},
# 	"edad":16,
# 	"correo":"regina@correo.org",
# 	"cursos":[
# 	    "Python",
# 	    "SQLModel",
# 	    "FastAPI"
# 	],
# 	"activo":true
# 	}"""

# # print(type(texto))
# mi_diccionario = json.loads(texto)
# pprint(mi_diccionario)
# # print(type(mi_diccionario))

# nuevo_json = json.dumps(mi_diccionario)
# print(nuevo_json)
# print("-->",type(nuevo_json))
# nuevo_json = json.dumps(mi_diccionario, indent=4)
# print(nuevo_json)