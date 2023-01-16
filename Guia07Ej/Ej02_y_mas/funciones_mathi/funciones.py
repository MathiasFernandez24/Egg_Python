import math


def area_circulo(radio:int):
    """Calcura el area de un circulo, recibe 1 parametro: -radio y retorna el area"""
    print(radio**2 * math.pi)
    return radio**2 * math.pi

def relacion(num1:int, num2:int):
    """Recibe 2 numeros, si el primero es mayor retorna 1, si el primero es menor retorna -1, si son iguales retorna 0"""
    if num1 > num2:
        print("retorna 1")
        return 1
    elif num1 < num2:
        print("retorna -1")
        return -1
    else:
        print("retorna 0")
        return 0

def separar(*args:int):
    """ recibe entreros (los que quieras, apaa...),(si viene en lista no olvides el asterisco delante)
    y retorna una tupla con 2 listas, l aprimera de pares y la segunda de impares"""
    pares = []
    impares = []
    for v in args:
        if (v % 2 == 0):
            pares.append(v)
        else:
            impares.append(v)
    pares.sort()
    impares.sort()
    print(pares, impares)
    return pares, impares

def validar_numero(num1:str):
    """
    recibe un string(numero), si es un entero retorna True, sino False
    """
    bandera = False
    simbolo = num1[0]
    if num1.isdigit():
        bandera = True
    elif simbolo == "-" or simbolo == "+":
        numerito = num1[1:]
        validacion = numerito.isdigit()
        bandera = validacion
    if bandera == True:
        numero_entero = int(num1)
        print(numero_entero, type(numero_entero))
    return bandera

def anio_bisiesto(anio:int):
    """recibe un entero(anio), si es bisiestro retorna True, sino False """
    validacion_1 = anio % 4 == 0
    validacion_2 = not (anio % 100 == 0)
    validacion_3 = anio % 400 == 0
    if validacion_1 and (validacion_2 or validacion_3):
        print("Es Año BISIESTRO")
        return True
    else:
        print("no es año bisiestro")
        return False

def tiempo(horas:int, minutos:int, segundos:int):
    """Ingresa Horas, minutos y segundos, los retorna ordenados en una tupla """
    dias = 0
    if segundos > 59:
        minutos = minutos + segundos // 60
        segundos = int(segundos % 60)
    if minutos > 59:
        horas = horas + minutos // 60
        minutos = int(minutos % 60)
    if horas > 23:
        dias = int(horas // 24)
        horas = int(horas % 24)
    print(f"""DD:{dias}
HH:{horas}
MM:{minutos}
SS:{segundos}""")
    return dias, horas, minutos, segundos

def validar_anio_bisiestro(num:str):
    """Valida un numero y chequea si es  anio bisiestro, no retorna, solo imprime con -->"""
    if validar_numero(num):
        print("--> Num validado correctamente")
        if anio_bisiesto(int(num)):
            print("--> anio es bisiestro")
        else:
            print("--> anio no es bisiestro")
    else:
        print("--> Num no validado")

def inputcito()->int:
    """ no recibe parametros, retorna un numero que el usuario ingrese por consola (tipo input)"""
    try:
        numero:int= int(input("Input: "))
        return int(numero)
    except ValueError:
        print("No se admiten palabras")
        return 0
    except Exception as e:
        print("Error nuevo, agregar a funcion inputcito",type(e))
        return 0