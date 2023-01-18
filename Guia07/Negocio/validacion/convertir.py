def a_int(dato):
    try:
        if not type(dato)== bool:
            return int(float(dato))
        else:
            raise  
    except Exception as e:
        return False

def a_float(dato):
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