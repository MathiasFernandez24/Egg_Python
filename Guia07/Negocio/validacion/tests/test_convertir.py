# from convertir import a_str, a_float, a_int
from validacion import convertir as c

def test_convertir_a_int():
    assert type(c.a_int(2))== int
    assert type(c.a_int(0))== int
    assert type(c.a_int(-90))== int
    assert type(c.a_int(-90.25))== int
    assert type(c.a_int(15.44590))== int
    assert type(c.a_int(0.00))== int
    assert type(c.a_int("-90"))== int
    assert type(c.a_int("3262"))== int
    assert type(c.a_int("-90.25"))== int
    assert type(c.a_int("15.44590"))== int
    assert type(c.a_int("0.00"))== int
    assert type(c.a_int("256"))== int
    assert type(c.a_int("-12"))== int
    assert type(c.a_int("0"))== int
    assert c.a_int("hola")== False
    assert c.a_int("-h")== False
    assert c.a_int("+h")== False
    assert c.a_int("+26h")== False
    assert c.a_int("-2a2h2ad")== False
    assert c.a_int("")== False
    assert c.a_int(True)== False
    assert c.a_int(False)== False

def test_convertir_a_float():
    assert type(c.a_float(2))== float
    assert type(c.a_float(0))== float
    assert type(c.a_float(-2))== float
    assert type(c.a_float(2.44))== float
    assert type(c.a_float(-6234.23435))== float
    assert type(c.a_float("-256"))== float
    assert type(c.a_float("-251.236"))== float
    assert type(c.a_float("0"))== float
    assert type(c.a_float("+25746"))== float
    assert type(c.a_float("+257.46"))== float
    assert c.a_float("+257.4we6")== False
    assert c.a_float("-257.4we6")== False
    assert c.a_float("hola")== False
    assert c.a_float("")== False
    assert c.a_float(True)== False
    assert c.a_float(False)== False
    
    
def test_convertir_a_str():
    assert type(c.a_str("123"))==str
    assert type(c.a_str("12asdsa"))==str
    assert type(c.a_str("asdasd123123"))==str
    assert type(c.a_str("--123"))==str
    assert type(c.a_str("+1asd23"))==str
    assert type(c.a_str(125))==str
    assert type(c.a_str(-125))==str
    assert type(c.a_str(12.5))==str
    assert type(c.a_str(-1.25))==str
    assert type(c.a_str(-1.25))==str
    assert type(c.a_str(-1.25))==str
    assert c.a_str(False)==False
    assert c.a_str(True)==False
    assert c.a_str(None)==False