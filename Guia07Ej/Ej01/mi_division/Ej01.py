def division():
    try:
        num_1:int = int(input("numero 1: "))
        num_2:int = int(input("numero 2: "))
        resultado= num_1/num_2    
        print(resultado)
    except ValueError:
        print("--Error, valor ingresado no valido")
    except ZeroDivisionError:
        print("--Error, el divisor no puede ser CERO")
    except Exception as e:
        print(type(e))
        print("--ERROR--")