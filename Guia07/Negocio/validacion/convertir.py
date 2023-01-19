def a_int(dato):
    """recibe cualquier tipo de dato, si es posible convertirlo en int, lo retorna, sino retorna False"""
    try:
        if not type(dato)== bool:
            return int(float(dato))
        else:
            raise  
    except Exception as e:
        return False

def a_float(dato):
    """recibe cualquier tipo de dato, si es posible convertirlo en float, lo retorna, sino retorna False"""
    try:
        if not type(dato)== bool:
            return float(dato)
        else:
            raise
    except Exception as e:
        return False

def a_str(dato):
    if type(dato) in [str,int,float]:
        return str(dato)
    else:
        return False

# print(int(90.99))   
# print(type(int(90.99)))   
# print(type(float(False)))
# print(float(False))