from typing import Any


def es_entero(entrada: Any) -> bool:
    try:
        entrada = str(entrada)
        if len(entrada) > 0:
            val_1: bool = entrada.isdigit()
            val_2: bool = entrada[0] in ("+", "-")
            val_3: bool = entrada[1:].isdigit()
            if val_1 or (val_2 and val_3):
                return True
        raise Exception
    except Exception:
        return False


# if __name__ == "__main__":
# def test_es_entero():
#     assert es_entero(10) == True
#     assert es_entero("10") == True
#     assert es_entero("+10") == True
#     assert es_entero("-10") == True
#     assert es_entero(10.10) == False
#     assert es_entero("10.10") == False
#     assert es_entero("texto") == False
#     assert es_entero("") == False
#     assert es_entero("+") == False
#     assert es_entero(["12, 123"]) == False

#     assert es_entero("-200a") == False
#     assert es_entero(" ") == False
