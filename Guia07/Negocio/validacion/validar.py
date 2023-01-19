from . import convertir as c


def entero_natural(numero):
    """recibe caalquier dato, si es posible convertirlo a un int mayor a cero (no incluye cero), retorna el int, sino retorna False"""
    r= c.a_int(numero)
    if r <= 0 :
        return False
    else:
        return r

def cadena_vacía(cadena:str):
    """recibe un string, si está vacio retorna False, sino retorna el string"""
    r = cadena.strip()
    if len(r) <= 0:
        return False
    else:
        return r

def real_positivo(numero:float):
    """ recibe caalquier dato, si es posible convertirlo a un float mayor a cero (no incluye cero), retorna el float, sino retorna False"""
    r = c.a_float(numero)
    if r <= 0 :
        return False
    else:
        return r

