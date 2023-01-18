
from validacion import validar as v

def test_validar_entero_natural():
    assert v.entero_natural("1") == 1
    assert v.entero_natural("+81") == 81
    assert v.entero_natural("7.89") == 7
    assert v.entero_natural("-51") == False
    assert v.entero_natural(0) == False
    assert v.entero_natural("0") == False
    assert v.entero_natural(-50) == False
    assert v.entero_natural("-100") == False

def test_validar_real_positivo():
    assert v.real_positivo("0.3") == 0.3
    assert v.real_positivo("+16.1603") == 16.1603
    assert v.real_positivo("+161603") == 161603.0
    assert v.real_positivo("0.3") == 0.3
    assert v.real_positivo("0") == False
    assert v.real_positivo("-0.2133") == False
    assert v.real_positivo("-as0.2133") == False
    assert v.real_positivo("+as0.21a33") == False

def test_validar_cadena_no_vacía():
    assert v.cadena_vacía("")==False
    assert v.cadena_vacía(" ")==False
    assert v.cadena_vacía("        ")==False
    assert v.cadena_vacía("   hola     ")== "hola"
    assert v.cadena_vacía("        chau")== "chau"
    assert v.cadena_vacía("   hola123    ")== "hola123"
