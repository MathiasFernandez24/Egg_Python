import paquete as p

def test_es_entero():
    assert p.es_entero(10) == True
    assert p.es_entero("10") == True
    assert p.es_entero("+10") == True
    assert p.es_entero("-10") == True
    assert p.es_entero(10.10) == False
    assert p.es_entero("10.10") == False
    assert p.es_entero("texto") == False
    assert p.es_entero("") == False
    assert p.es_entero("+") == False
    assert p.es_entero(["12, 123"]) == False

    assert p.es_entero("-200a") == False
    assert p.es_entero(" ") == False

def test_mathi():
    assert True

def test_mai():
    assert True

def test_maxi():
    assert True