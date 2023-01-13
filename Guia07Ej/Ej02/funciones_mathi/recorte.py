def recortar(numero:int, min:int, max:int):
    """recibe un numero, un minimo y un maximo, si el numero está entre 
    el minimo y el maximo, retorna el numero, si esta por debajo del minimo 
    retorna el minimo y si está por encima del maximo retorna el maximo"""
    if numero < min:
        return min
    elif numero > max:
        return max
    else:
        return numero