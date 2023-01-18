from . import convertir as c


def entero_natural(numero):
    r= c.a_int(numero)
    if r <= 0 :
        return False
    else:
        return r

def cadena_vacía(cadena):
    r = cadena.strip()
    if len(r) <= 0:
        return False
    else:
        return r

def real_positivo(numero):
    r = c.a_float(numero)
    if r <= 0 :
        return False
    else:
        return r

