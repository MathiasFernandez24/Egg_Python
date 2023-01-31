import os

# variable_1 = "mi_ruta.txt"
# variable_2 = os.getcwd()
# print(os.path.isfile(variable_1))
# print("+++",variable_2)

def crear_Archivo(nombre_archivo):
    if os.path.isfile(nombre_archivo):
        print("El archivo ya existe")
    else:
        with open(nombre_archivo,"w"):
            print(f"Se creó el archivo culero llamado: {nombre_archivo}")

def sobreescribir(nombre_archivo, texto):
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo,"w") as f:
            f.write(texto)
            print(f"Se sobreescribio el archivo culero llamado: {nombre_archivo}") 
    else:
        print("El archivo no existe")


crear_Archivo("archivo_01.txt")
sobreescribir("archivo_01.txt","hola, soy una sobreescritura")