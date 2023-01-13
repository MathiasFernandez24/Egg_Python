import math


def area_rectangulo(base, altura):
    """Calcula el area de un rectangulo, recibe 2 parametros:-base-Altura"""
    print("--->", base*altura)
    return base*altura


def area_circulo(radio):
    """Calcura el area de un circulo, recibe 1 parametro: -radio"""
    return radio**2 * math.pi


def relacion(num1, num2):
    """Recibe 2 numeros, si el primero es mayor retorna 1, si el primero es menor retorna -1, si son iguales retorna 0"""
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


def intermedio(num1, num2):
    """Recibe 2 numero y retorna el promedio"""
    return (num1+num2)/2


def recortar(numero, min, max):
    if numero < min:
        return min
    elif numero > max:
        return max
    else:
        return numero


def separar(*args):
    pares = []
    impares = []
    for v in args:
        if (v % 2 == 0):
            pares.append(v)
        else:
            impares.append(v)
    pares.sort()
    impares.sort()
    return pares, impares


def ejocho(num1):
    """
    Aqui va la documentacion de la funcion
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
        print(numero_entero)
        anio_bisiesto(numero_entero)
    return bandera


#  año bisiestro
def anio_bisiesto(anio):
    validacion_1 = anio % 4 == 0
    validacion_2 = not (anio % 100 == 0)
    validacion_3 = anio % 400 == 0
    if validacion_1 and (validacion_2 or validacion_3):
        print("Es Año BISIESTRO")
        return True
    else:
        print("no es año bisiestro")
        return False


def ejnueve(horas, minutos, segundos):
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


# {
#     "artículo": {
#         {
#             "id": int,
#             "nombre": str,
#             "precio": float,
#             "cantidad": int
#         },
#     }
# }


a = area_rectangulo(2, 4)
a = area_circulo(2)
a = relacion(2, 5)
a = intermedio(2.5, 5.4)
a = recortar(1, 5, 10)
# a = ejocho("+2000")
# a = ejnueve(23, 59, 120)
# print(a)

b = [5, 8, 1, 3, 5, 9, 15, 4, 3]
c = separar(*b)

# p = [p for p in b if p % 2 == 0]
# i = [i for i in b if i % 2 == 1]
# print(p)
# print(i)
