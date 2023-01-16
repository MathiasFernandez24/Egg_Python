def recortar(numero:int, min:int, max:int):
    """recibe un numero, un minimo y un maximo, si el numero está entre 
    el minimo y el maximo, retorna el numero, si esta por debajo del minimo 
    retorna el minimo y si está por encima del maximo retorna el maximo"""
    if numero < min:
        print(min)
        return min
    elif numero > max:
        print(max)
        return max
    else:
        print(numero)
        return numero