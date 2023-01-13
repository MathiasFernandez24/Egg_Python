try:
    a = int(input("a: "))
    b = int(input("b: "))
    division = a/b
except TypeError:
    print("Error, operando no permite la division")
except ZeroDivisionError:
    # raise ZeroDivisionError("Error, división por cero")
    print("Error, division por cero")
except NameError:
    print("Error, variable no definida")
except Exception as e:
    print("Error desconocido --> ", type(e).__name__)
else:
    print(f"El resultado de la division es {division}")
finally:
    print("Siempre se ejecuta Finally")
