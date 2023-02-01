from dataclasses import dataclass, asdict
from datetime import datetime
import locale
import datetime as dt 

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
    texto = f"Nombre: {diccionario['nombres']}, Apellido: {diccionario['apellidos']}, DNI: {diccionario['dni']}, Fecha de Nacimiento: {diccionario['nacimiento']}"
    fecha_creacion= datetime.today()
    fecha_creacion=fecha_creacion.strftime(" - Creado: %A %d/%B/%Y %H:%M:%S")
    texto=texto+fecha_creacion

    with open("cliente.txt","a") as a:
        a.write(texto + "\n")

c_01 = cliente_crear()
cliente_guardar(c_01)
































# from datetime import date, time, datetime as dt, timedelta
# import datetime
# import locale

# locale.setlocale(locale.LC_ALL, "es_AR") 

# print(date(2023, 1, 1))
# print(datetime.date(2025, 12, 25))

# print(time(14, 30, 1))
# print(datetime.time(14, 30, 1))

# print(dt(2023, 12, 31, 23, 59, 59))
# print(datetime.datetime(1914, 8, 20, 14, 30, 1))
# print(dt(1991, 3, 25, 14, 30, 1))


# # dat = datetime()
# fecha = dt.now()
# print(fecha.microsecond)
# print(fecha.weekday())

# print(dt.today())
# print(dt.now())
# print(fecha.strftime("%y - %B - %A - %H - %I - %C"))
# f_01 = fecha.strftime("%y")

# f_02=dt.strptime("6/2/2023","%d/%m/%Y")
# f_03=dt.strptime("2023","%Y")

# # print(f_02)
# print(f_02)
# print(f_03)

# mi_nacimiento = dt(1986, 10, 15)
# print(mi_nacimiento)
# # print(mi_nacimiento + timedelta(32, 3600))
# print(dt.now() - mi_nacimiento)
# print(mi_nacimiento > dt.now())
# mi_edad = dt.now() - mi_nacimiento 
# print(mi_edad)

# print(timedelta(31, 3600))